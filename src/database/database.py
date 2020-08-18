#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

from MySQLdb import MySQLError, connect

from decouple import config

from messages_controller import MessagesController, extract_chat_object, extract_user_object
from models.chat import Chat
from models.user import User


class Database():
    def __init__(self):
        self.messages_controller = MessagesController()
        self.cursor = None
        self.db = None
        self.connect()
        self.db.ping(True)

    def connect(self):
        db = connect(passwd=config("DB_PASSWORD"), db=config("DB_NAME"),
                             user=config("DB_USER"), host=config("DB_HOST"))
        self.cursor = db.cursor()
        self.db = db

    def update(self, telegram_message):
        chat = extract_chat_object(telegram_message)
        user = extract_user_object(telegram_message)

        if not self.find_chat(chat.chat_id):
            self.insert_chat(chat)
        if not self.find_chat(chat.chat_id):
            self.insert_chat(chat)

        if not self.find_user(user.telegram_id):
            self.insert_user(user)

    def find_chat(self, chat_id):
        self.db.ping(True)
        query = f"""SELECT * FROM chats WHERE chat_id={chat_id} """
        if self.cursor.execute(query) == 0:
            return None
        chat_db = self.cursor.fetchone()
        return Chat(
            chat_id=chat_db[1],
            title=chat_db[2],
            chat_type=chat_db[3]
        )

    def find_user(self, telegram_id):
        self.db.ping(True)
        query = f"""SELECT * FROM users WHERE telegram_id={telegram_id} """
        if self.cursor.execute(query) == 0:
            return None
        user_db = self.cursor.fetchone()
        return User(
            telegram_id=user_db[1],
            is_bot=user_db[2],
            first_name=user_db[3],
            last_name=user_db[4],
            username=user_db[5]

        )

    def insert_chat(self, chat):
        self.db.ping(True)
        query = f"""INSERT INTO chats (chat_id, title, chat_type)
                    VALUES ({int(chat.chat_id)}, "{chat.title}", "{chat.chat_type}");"""
        print(chat.chat_id, chat.title, chat.chat_type)
        self.cursor.execute(query)
        self.db.commit()

    def insert_user(self, user):
        self.db.ping(True)
        query = f"""INSERT INTO users (telegram_id, is_bot, first_name, last_name, username)
                    VALUES ({user.telegram_id}, "{int(user.is_bot)}", "{user.first_name}", "{user.last_name}", "{user.username}");"""
        self.cursor.execute(query)
        self.db.commit()

    def find_experience_points(self, user_telegram_id, chat_id):
        self.db.ping(True)
        query = f"""SELECT experience_points FROM experiences 
        WHERE user_telegram_id = {int(user_telegram_id)} AND chat_id = {int(chat_id)};"""
        self.cursor.execute(query)
        experience_points = self.cursor.fetchone()
        if experience_points:
            return experience_points[0]
        else:
            return 0

    def add_user_experience(self, user_telegram_id, experience, chat_id):
        self.db.ping(True)
        current_experience_points = self.find_experience_points(
            user_telegram_id, chat_id)
        new_experience_points = current_experience_points + experience
        if current_experience_points == 0:
            query = f"""INSERT INTO experiences (user_telegram_id, experience_points, chat_id)
                        VALUES ({int(user_telegram_id)}, {int(new_experience_points)}, {int(chat_id)});"""
        else:
            query = f"""UPDATE experiences SET experience_points = {int(new_experience_points)}
                        WHERE user_telegram_id = {int(user_telegram_id)} AND 
                        chat_id = {int(chat_id)};"""
        self.cursor.execute(query)
        self.db.commit()

    def get_experiences(self, chat_id, amount=10):
        self.db.ping(True)
        query = f"""SELECT u.first_name, u.last_name, u.username, e.experience_points
                    FROM experiences AS e
                    INNER JOIN chats AS c
                    ON e.chat_id = c.chat_id 
                    INNER JOIN users AS u
                    ON e.user_telegram_id = u.telegram_id
                    WHERE e.chat_id = {chat_id}
                    AND u.is_bot = 0
                    ORDER BY e.experience_points DESC
                    LIMIT {amount}"""
        self.cursor.execute(query)
        experiences_db = self.cursor.fetchall()
        response = "Experiências: \n\n"
        for experience in experiences_db:
            first_name = experience[0]
            last_name = experience[1]
            username = experience[2]
            experience = experience[3]
            response += f"{first_name} {last_name} ({experience})\n"
        return response

    def get_user_level(self, user_telegram_id, chat_id):
        experience_points = self.find_experience_points(user_telegram_id = user_telegram_id, chat_id = chat_id)
        user_level = 0
        level_requirement = 0
        while experience_points > level_requirement:
            user_level += 1
            level_requirement = round((user_level ** 2) - user_level + 15 + level_requirement)
        return user_level

