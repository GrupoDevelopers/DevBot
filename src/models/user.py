#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################


class User:
    def __init__(self, telegram_id, first_name, last_name, username, is_bot):
        self.telegram_id = telegram_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_bot = is_bot

    def __eq__(self, other):
        return self.telegram_id == other.telegram_id
