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


    def handle(self, mproto_query, user_id):
        if 'code' not in mproto_query:
            return self.__sender.send_150('Отстуствует поле "code"')

        code = mproto_query["code"]
        if self.__codes.get(f'{code}') is None:
            return self.__sender.send_150(f'Не существует кода {code} в протоколе MProto')
    
        try:
            return self.__codes[f'{code}'](mproto_query, user_id)
        except DBConnectionException:
            return self.__sender.send_151()


    def handle20(self, mproto_query, user_id_):
        user_id = user_id_
        return self.__sender.send_120(self.__dbhandler.getDialogsByUserId(user_id))


    def handle21(self, mproto_query, user_id_):
        dialog_id = user_id_
        return self.__sender.send_121(self.__dbhandler.getMessagesByDialogId(dialog_id))

    
    def _getIdAndPasswordByLogin(self, user_login):
        return self.__dbhandler.getIdAndPasswordByLogin(user_login)