#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import logging

from aiogram import types, Bot

from bot_behaviors.random_responses import random_response
from bot_behaviors.experience import Experience
from database.database import Database
from decouple import config
bot = Bot(token= config('API_TOKEN'))

class DevBot:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.bot = bot
        self.database = Database()
        self.experience = Experience(self.database)
        self.run_bot()

    def run_bot(self):
        @self.dispatcher.message_handler(commands=['exp'])
        async def exp(message: types.Message):
            response = self.database.get_experiences(chat_id=message.chat.id)
            await message.reply(response)

        @self.dispatcher.message_handler()
        async def listening(message: types.Message):
            await random_response(message)
            self.database.update(message)
            self.experience.handler(message)
