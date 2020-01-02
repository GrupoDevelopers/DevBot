#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import logging

from aiogram import Bot, Dispatcher, executor, types
from decouple import config
from dev_bot import DevBot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    API_TOKEN = config('API_TOKEN')
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    main = DevBot(dp)
    executor.start_polling(dp, skip_updates=True)
