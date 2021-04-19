from connector import Connector

class DBHandler:

    __connector = None

    def __init__(self):
        self.__connector = Connector()


    # Возвращает информацию о диалогах, в которых состоит пользователь user_id
    def getDialogsByUserId(self, user_id):
        cursor = self.__connector.getCursor()
        cursor.execute(f'SELECT dialog_id from dialogs_info where user_id={user_id}')
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
        cursor = self.__connector.getCursor()
        cursor.execute(f'SELECT type, avatar from dialogs where dialog_id={dialog_id}')
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
                'time': lstmsg[3],
                'status':lstmsg[4] 
            }

        result = {
            'dialog_id': dialog_id,
            'type': dialog[0],
            'avatar': dialog[1],
            'lastMsg': lastMsg
            }

        return result