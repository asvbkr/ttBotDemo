# -*- coding: UTF-8 -*-
from TamTamBot.TamTamBot import TamTamBot
from ttBotDemo.BotCfg import TOKEN


class Bot(TamTamBot):
    @property
    def token(self):
        # type: () -> str
        return TOKEN


bot = Bot()
bot.polling()
