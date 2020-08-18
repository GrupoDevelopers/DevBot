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
            try:
                member = await bot.get_chat_member(chat_id=str(chatid), user_id=str(userid))
                name_member = member['user']['first_name']
                if ("last_name" in member['user']): f"{name_member} {member['user']['last_name']}"
                return name_member
            except:
                return "Conta Excluida"
            
        @self.dispatcher.message_handler(commands=['exp'])
        async def exp(message: types.Message):
            experiences_db = await self.database.get_experiences(chat_id=message.chat.id)
            response, cont = "Experiências:\n\n", 0
            for item in experiences_db:
                name_member_data = await check_name_member(experiences_db[cont]['chat_id'], experiences_db[cont]['telegram_id'])
                response += f"{name_member_data} ({experiences_db[cont]['experience_points']})\n"
                cont = cont + 1
            await message.reply(response)

        @self.dispatcher.message_handler()
        async def listening(message: types.Message):
            await random_response(message)
            if (message.chat.type != "private"):
                await self.database.update(message)
                await self.experience.handler(message)
