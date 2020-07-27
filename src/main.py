#########################################################################
#                                                                       #
#                       Grupo Developers                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################

import logging

from aiogram import Dispatcher, executor, types
from dev_bot import DevBot, bot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher(bot)
    main = DevBot(dp)
    executor.start_polling(dp, skip_updates=True)
