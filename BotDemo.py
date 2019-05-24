# -*- coding: UTF-8 -*-
import logging

from TamTamBot.TamTamBot import TamTamBot


class BotDemo(TamTamBot):
    def __init__(self):
        super(BotDemo, self).__init__()
        self.debug = True
        self.logging_level = logging.DEBUG if self.debug else logging.INFO

    @property
    def token(self):
        # type: () -> str
        # noinspection SpellCheckingInspection
        return 'VCur56yHIOgz7O5otyduM_rHHlQ3k9SYE0uc6_mRadM'


if __name__ == '__main__':
    bot = BotDemo()
    bot.polling()
