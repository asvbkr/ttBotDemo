# -*- coding: UTF-8 -*-
import logging
import os

from TamTamBot.TamTamBot import TamTamBot


class BotDemo(TamTamBot):

    @property
    def token(self):
        # type: () -> str
        token = os.environ.get('TT_BOT_DEMO_API_TOKEN')
        return token


if __name__ == '__main__':
    bot = BotDemo()
    bot.polling()
