#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import logging

from aiogram import types

from bot_behaviors.random_responses import random_response
from bot_behaviors.experience import Experience
from database.database import Database


class DevBot:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.database = Database()
        self.experience = Experience(self.database)
        self.run_bot()

    def run_bot(self):
        @self.dispatcher.message_handler()
        async def listening(message: types.Message):
            await random_response(message)
            self.database.update(message)
            self.experience.handler(message)

            if '/exp' in message.text.lower():
                response = self.database.get_experiences(chat_id=message.chat.id)
                await message.reply(response)
