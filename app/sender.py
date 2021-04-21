
class Sender:
    
    def send_150(self, text):
        msg = f"Ошибка в протоколе: {text}"
        return {
            'code': 150,
            'msg': msg
        }


    def send_151(self, text=''):
        msg = f"Соединение с базой данных потеряно... {text}"
        return {
            'code': 151,
            'msg': msg
        }


    def send_120(self, dialogs):
        return {
            'code': 120,
            'dialogs': dialogs["dialogs"]
        }


    def send_121(self, messages):
        return {
            'code': 121,
            'lastMsgInf': messages["lastMsgInf"],
            'messages': messages["messages"]
        }