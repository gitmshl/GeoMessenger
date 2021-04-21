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

    '''
        {
            lastMsgInf: {
                'id': ,
                'from': ,
                'msg': ,
                'time': ,
                'status': 
            }
            messages: [
                    {
                        id:
                        user_id:
                        msg: 
                        picture:
                        time:
                        status:
                        from_user_login:
                        from_user_name:
                        from_user_avatar:
                    }, ....
            ]
        }
        
    '''

    def getMessagesByDialogId(self, dialog_id):
        try:
            cursor = self.__connector.getCursor()
            #cursor.execute(f'select id, user_id, msg, picture, time, status from messages where dialog_id = {dialog_id}')
            cursor.execute(f'select m.*, u.login, u.name, u.avatar from messages m, users u where m.user_id = u.user_id and m.dialog_id = {dialog_id} order by m.time')
        except Exception:
            raise DBConnectionException
        
        messages = []
        for msg in cursor.fetchall():
            message = {
                'id': msg[0],
                'user_id': msg[2],
                'msg': msg[3],
                'picture': msg[4],
                'time': msg[5].isoformat(),
                'status': msg[6],
                'from_user_login': msg[7],
                'from_user_name': msg[8],
                'from_user_avatar': msg[9]
            }
            messages.append(message)
        
        lastMsgInf = self.getLastMsgInDialog(dialog_id)

        result = {
            'messages': messages,
            'lastMsgInf': lastMsgInf
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
            result["dialogs"].append(self.getDialogInformation(dialog, user_id))

        return result


    # Возвращает информацию про диалог по его id. Если такого диалога нету, то возвращается None
    '''
        {
            dialog_id:
            dialog_name:
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
    def getDialogInformation(self, dialog_id, user_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT type, avatar from dialogs where dialog_id={dialog_id}')
            dialog = cursor.fetchone()           
            if dialog is None: return None
            dialog_res = self.getDialogNameAndAvatar(dialog_id, user_id)

            if dialog_res is None:
                print('ИМЯ ДИАЛОГА NONE. ЭТО ОЧЕНЬ СТРАННО!!!!')
                dialog_name = 'undefined'
                dialog_avatar = ''
            else:
                dialog_name, dialog_avatar = dialog_res
            
            cursor.execute(f'select id, user_id, msg, time, status from messages where dialog_id = {dialog_id} order by time desc limit 1;')
            lstmsg = cursor.fetchone()
        except Exception:
            raise DBConnectionException

        
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
            'dialog_name': dialog_name,
            'type': dialog[0],
            'avatar': dialog_avatar,
            'lastMsg': lastMsg
            }

        return result


    def getDialogNameAndAvatar(self, dialog_id, user_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT type, dialog_name, avatar from dialogs where dialog_id={dialog_id}')

            res = cursor.fetchone()
            if res is None: return None
            dialog_type, dialog_name, dialog_avatar = res[0], res[1], res[2]
            if dialog_type == 'dialog': return (dialog_name, dialog_avatar)

            cursor.execute(f'select user_id from dialogs_info where dialog_id = {dialog_id} and user_id != {user_id}')         
            another_user = cursor.fetchone()
            if another_user is None: return None
            another_user_id = another_user[0]
            return (self.getUserNameById(another_user_id), self.getUserAvatarById(another_user_id))

        except Exception:
            raise DBConnectionException


    def getUserAvatarById(self, user_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT avatar from users where user_id={user_id}')
            res = cursor.fetchone()
            if res is None: return ''
            return res[0]
        except Exception:
            raise DBConnectionException


    def getUserNameById(self, user_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'SELECT name from users where user_id={user_id}')
            res = cursor.fetchone()
            if res is None: return None
            return res[0]
        except Exception:
            raise DBConnectionException


    def getLastMsgInDialog(self, dialog_id):
        try:
            cursor = self.__connector.getCursor()
            cursor.execute(f'select id, user_id, msg, time, status from messages where dialog_id = {dialog_id} order by time desc limit 1;')
            lstmsg = cursor.fetchone()
            if lstmsg is None: return {}
            else:
                lstmsg = {
                'id': lstmsg[0],
                'from': lstmsg[1],
                'msg': lstmsg[2],
                'time': lstmsg[3].isoformat(),
                'status':lstmsg[4] 
                }
                return lstmsg

        except Exception:
            raise DBConnectionException