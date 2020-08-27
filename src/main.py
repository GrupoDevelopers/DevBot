#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import logging

from aiogram import types, Bot, Dispatcher, executor

from bot_behaviors.random_responses import random_response
from bot_behaviors.experience import Experience
from database.database import Database
from aiogram.utils.emoji import emojize

from decouple import config

class DevBot:
    def __init__(self):
        self.bot = Bot(token= config('API_TOKEN'))
        self.database = Database()
        self.dispatcher = Dispatcher(self.bot)
        self.experience = Experience(self.database)
        self.run_bot()

    def run_bot(self):
        async def check_name_member(chatid, userid):
            try:																	
                member = await self.bot.get_chat_member(chat_id=str(chatid), user_id=str(userid))
                name_member = member['user']['first_name']
                if ("last_name" in member['user']): name_member = f"{name_member} {member['user']['last_name']}"
                return name_member
            except:																																																																																																											
                return "Conta Excluida"
            
        @self.dispatcher.message_handler(commands=['exp'])
        async def exp(message: types.Message):
            response, cont = ":trophy: Ranking de experiência :trophy:\n\n", 0
            experiences_db = await self.database.get_experiences(chat_id=message.chat.id)
            for item in experiences_db:
                name_member_data = await check_name_member(experiences_db[cont]['chat_id'], experiences_db[cont]['telegram_id'])
                member_level, level_req = await self.database.get_user_level(user_telegram_id= experiences_db[cont]['telegram_id'], chat_id= experiences_db[cont]['chat_id'])
                response += f"{name_member_data} - Nível {member_level} ({experiences_db[cont]['experience_points']}/{level_req})\n"
                cont = cont + 1
            await message.reply(emojize(response))

        @self.dispatcher.message_handler()
        async def listening(message: types.Message):
            await random_response(message)
            if (message.chat.type != "private"):
                await self.database.update(message)
                await self.experience.handler(message)																																																																																									
                
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[\033[92m%(asctime)s\033[0m] - %(levelname)s : %(message)s', 
                        datefmt='%H:%M:%S')
    executor.start_polling(DevBot().dispatcher, skip_updates=True)