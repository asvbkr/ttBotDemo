# -*- coding: UTF-8 -*-
import logging
import os

from TamTamBot.TamTamBot import TamTamBot


class BotDemo(TamTamBot):
    def __init__(self):
        super(BotDemo, self).__init__()
        self.debug = True
        self.logging_level = logging.DEBUG if self.debug else logging.INFO

    @property
    def token(self):
        # type: () -> str
        token = os.environ.get('TT_BOT_DEMO_API_TOKEN')
        return token


if __name__ == '__main__':
    bot = BotDemo()
    bot.polling()
