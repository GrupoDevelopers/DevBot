#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################


class Message:
    def __init__(self, message_id, text, date, chat_id, author_id, reply_message_id):
        self.message_id = message_id
        self.text = text
        self.date = date
        self.chat_id = chat_id
        self.author_id = author_id
        self.reply_to_message = reply_message_id

    def __eq__(self, other):
        return self.message_id == other.message_id and self.date == other.date
