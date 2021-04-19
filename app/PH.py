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
            '20': self.handle20,
            '21': self.handle21
        }


    def handle(self, mproto_query):
        if 'code' not in mproto_query:
            return self.__sender.send_150('Отстуствует поле "code"')

        code = mproto_query["code"]
        if self.__codes.get(f'{code}') is None:
            return self.__sender.send_150(f'Не существует кода {code} в протоколе MProto')
    
        try:
            return self.__codes[f'{code}'](mproto_query)
        except DBConnectionException:
            return self.__sender.send_151()


    def handle20(self, mproto_query):
        user_id = mproto_query["from"]
        return self.__sender.send_120(self.__dbhandler.getDialogsByUserId(user_id))


    def handle21(self, mproto_query):
        dialog_id = mproto_query["dialog_id"]
        return self.__sender.send_121(self.__dbhandler.getMessagesByDialogId(dialog_id))