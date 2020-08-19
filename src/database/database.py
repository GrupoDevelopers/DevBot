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
        self.connect()

    def connect(self):
        self.db = connect(host=config("DB_HOST"), db=config("DB_NAME"),
                            user=config("DB_USER"),passwd=config("DB_PASSWORD"))
        self.messages_controller = MessagesController()
        self.cursor = self.db.cursor()
        self.ping = self.db.ping(True)

    def chat_exists(self, chat_id):
        self.ping
        check_chat = self.cursor.execute(f"SELECT * FROM chats WHERE chat_id={chat_id}")
        if (check_chat == 0):
            return False
        return self.cursor.fetchone()

    def user_exists(self, telegram_id):
        self.ping
        check_user = self.cursor.execute(f"SELECT * FROM users WHERE telegram_id={telegram_id}")
        if (check_user == 0):
            return False
        return self.cursor.fetchone()

    async def update(self, telegram_message):
        self.ping
        chat = extract_chat_object(telegram_message)
        user = extract_user_object(telegram_message)
        if (self.chat_exists(chat.chat_id)) == False:
           await self.insert_chat(chat)
        if (self.user_exists(user.telegram_id)) == False:
           await self.insert_user(user)

    async def insert_chat(self, chat):
        self.ping
        self.cursor.execute(f"INSERT INTO chats (chat_id) VALUES ({int(chat.chat_id)});")
        self.db.commit()

    async def insert_user(self, user):
        self.ping
        self.cursor.execute(f"INSERT INTO users (telegram_id) VALUES ({user.telegram_id});")
        self.db.commit()

    async def find_experience_points(self, user_telegram_id, chat_id):
        self.ping
        self.cursor.execute(f"SELECT experience_points FROM experiences \
            WHERE user_telegram_id = {int(user_telegram_id)} AND chat_id = {int(chat_id)};")
        experience_points = self.cursor.fetchone()
        if (experience_points):
            return experience_points[0]
        else:
            return False

    async def add_user_experience(self, user_telegram_id, experience, chat_id):
        self.ping
        current_experience_points = await self.find_experience_points(user_telegram_id, chat_id)
        new_experience_points = current_experience_points + experience
        if (current_experience_points == False):
            query = f"""INSERT INTO experiences (user_telegram_id, experience_points, chat_id)
                        VALUES ({int(user_telegram_id)}, {int(new_experience_points)}, {int(chat_id)});"""
        else:
            query = f"""UPDATE experiences SET experience_points = {int(new_experience_points)}
                        WHERE user_telegram_id = {int(user_telegram_id)} AND 
                        chat_id = {int(chat_id)};"""
        self.cursor.execute(query)
        self.db.commit()

    async def get_experiences(self, chat_id, amount=10):
        self.ping
        self.cursor.execute(f"""SELECT u.telegram_id, c.chat_id, e.experience_points
                    FROM experiences AS e
                    INNER JOIN chats AS c
                    ON e.chat_id = c.chat_id 
                    INNER JOIN users AS u
                    ON e.user_telegram_id = u.telegram_id
                    WHERE e.chat_id = {chat_id}
                    ORDER BY e.experience_points DESC
                    LIMIT {amount}""")
        experience_data, experiences_db = [], self.cursor.fetchall()
        for item in experiences_db:
            experience_data.append({"telegram_id":item[0], "chat_id":item[1], "experience_points":item[2]})
        return experience_data

    def get_user_level(self, user_telegram_id, chat_id):
        experience_points = self.find_experience_points(user_telegram_id = user_telegram_id, chat_id = chat_id)
        user_level = 0
        level_requirement = 0
        while experience_points > level_requirement:
            user_level += 1
            level_requirement = round((user_level ** 2) - user_level + 15 + level_requirement)
        return user_level
