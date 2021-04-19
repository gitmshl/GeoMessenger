from DBHandler import DBHandler
from sender import Sender
from custom_exceptions import *

class PH:
    __dbhandler = None
    __sender = None
    __codes = {}

    def __init__(self):
        self.__dbhandler = DBHandler()
        self.__sender = Sender()
        self.__codes = {
            '20': self.handle20
        }

    def handle(self, mproto_query):
        if 'code' not in mproto_query:
            self.__sender.send_150('Отстуствует поле "code"')
            return

        code = mproto_query["code"]
        if self.__codes.get(f'{code}') is None:
            self.__sender.send_150(f'Не существует кода {code} в протоколе MProto')
            return

        self.__codes[f'{code}'](mproto_query)

    def handle20(self, mproto_query):
        user_id = mproto_query["from"]
        self.__sender.send_120(self.__dbhandler.getDialogsByUserId(user_id))