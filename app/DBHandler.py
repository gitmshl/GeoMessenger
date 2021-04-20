from connector import Connector
from custom_exceptions import DBConnectionException

class DBHandler:

    __connector = None

    def __init__(self):
        self.__connector = Connector()


    def getIdAndPasswordByLogin(self, user_login):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'select user_id, password from users where login = \'{user_login}\'')
        except Exception:
            raise DBConnectionException
        res = cursor.fetchone()
        return res


    # Возвращает список сообщений в диалоге
    def getMessagesByDialogId(self, dialog_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'select id, user_id, msg, picture, time, status from messages where dialog_id = {dialog_id}')
        except Exception:
            raise DBConnectionException
        
        messages = []
        for msg in cursor.fetchall():
            message = {
                'id': msg[0],
                'user_id': msg[1],
                'msg': msg[2],
                'picture': msg[3],
                'time': msg[4].isoformat(),
                'status': msg[5]
            }
            messages.append(message)
        
        result = {
            'messages': messages
        }

        return result


    # Возвращает информацию о диалогах, в которых состоит пользователь user_id
    def getDialogsByUserId(self, user_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT dialog_id from dialogs_info where user_id={user_id}')
        except Exception:
            raise DBConnectionException

        dialogs = []
        for dialog_id in cursor.fetchall():
            dialogs.append(dialog_id[0])
        result = {'dialogs': []}
        
        for dialog in dialogs:
            result["dialogs"].append(self.getDialogInformation(dialog))

        return result


    # Возвращает информацию про диалог по его id. Если такого диалога нету, то возвращается None
    '''
        {
            dialog_id: 
            avatar: 
            lastMsg = {
                'id': ,
                'from': ,
                'msg': ,
                'time': ,
                'status': 
            }
        }
    '''
    def getDialogInformation(self, dialog_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT type, avatar from dialogs where dialog_id={dialog_id}')
        except Exception:
            raise DBConnectionException
        
        dialog = cursor.fetchone()
        
        if dialog is None: return None

        cursor.execute(f'select id, user_id, msg, time, status from messages where dialog_id = {dialog_id} order by time desc limit 1;')
        lstmsg = cursor.fetchone()

        if lstmsg is None:
            lastMsg = {}
        else:
            lastMsg = {
                'id': lstmsg[0],
                'from': lstmsg[1],
                'msg': lstmsg[2],
                'time': lstmsg[3].isoformat(),
                'status':lstmsg[4] 
            }

        result = {
            'dialog_id': dialog_id,
            'type': dialog[0],
            'avatar': dialog[1],
            'lastMsg': lastMsg
            }

        return result