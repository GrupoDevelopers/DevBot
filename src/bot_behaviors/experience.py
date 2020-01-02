#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

from messages_controller import MessagesController

MAX_MESSAGES = 10


class Experience:
    def __init__(self, database):
        self.messages_controller = MessagesController()
        self.database = database

    def handler(self, telegram_message):
        self.messages_controller.add(telegram_message)
        chats = self.messages_controller.chats
        for chat in chats:
            if len(chat.messages) > MAX_MESSAGES:
                self.distribute_experience_points(chat)
                self.messages_controller.autoclear()

    def distribute_experience_points(self, chat):
        user_amount_messages = users_message_count(chat)
        experience_points = calculate_experience_points(user_amount_messages)
        for user_telegram_id, experience in experience_points.items():
            self.database.add_user_experience(user_telegram_id, experience, chat.chat_id)


def calculate_experience_points(user_amount_messages):
    experience_points = {}
    for user_telegram_id, user_amount in user_amount_messages.items():
        experience_points[user_telegram_id] = user_amount * 1
    return experience_points


def users_message_count(chat):
    user_message_count = {}
    for message in chat.messages:
        if user_message_count.get(message.author_id):
            user_message_count[message.author_id] += 1
        else:
            user_message_count[message.author_id] = 1
    return user_message_count
