# -*- coding: UTF-8 -*-
import logging

from TamTamBot.TamTamBot import TamTamBot
from ttBotDemo.BotCfg import TOKEN


class BotDemo(TamTamBot):
    @property
    def token(self):
        # type: () -> str
        return TOKEN

    @property
    def debug(self):
        return logging.DEBUG

    @property
    def logging_level(self):
        return True


if __name__ == '__main__':
    bot = BotDemo()
    bot.polling()
