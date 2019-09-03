# -*- coding: UTF-8 -*-
import logging
import os

from TamTamBot.TamTamBot import TamTamBot
from TamTamBot.utils.lng import set_use_django


class BotDemo(TamTamBot):

    @property
    def description(self):
        # type: () -> str
        return 'Простейший бот на python. Исходный код - https://github.com/asvbkr/ttBotDemo.\n\n' \
               'Simple bot in python. Source code - https://github.com/asvbkr/ttBotDemo.'

    @property
    def token(self):
        # type: () -> str
        token = os.environ.get('TT_BOT_DEMO_API_TOKEN')
        return token


if __name__ == '__main__':
    set_use_django(False)
    bot = BotDemo()
    bot.polling()
