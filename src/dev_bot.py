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
        async def check_name_member(chatid, userid):
            member = await bot.get_chat_member(chat_id=str(chatid), user_id=str(userid))
            return member['user']['first_name']
            
        @self.dispatcher.message_handler(commands=['exp'])
        async def exp(message: types.Message):
            experiences_db = self.database.get_experiences(chat_id=message.chat.id)
            response = "Experiências:\n\n"
            for member_data in experiences_db:
                re = await check_name_member(member_data[1], member_data[0])
                response += f"{re} ({member_data[2]})\n"
            await message.reply(response)

        @self.dispatcher.message_handler()
        async def listening(message: types.Message):
            await random_response(message)
            self.database.update(message)
            self.experience.handler(message)
