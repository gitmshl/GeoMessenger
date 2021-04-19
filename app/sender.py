
class Sender:
    
    def send_150(self, text):
        msg = f"Ошибка в протоколе: {text}"
        print('send150', msg)


    def send_151(self, text=''):
        msg = f"Соединение с базой данных потеряно... {text}"
        print('send 151', msg)


    def send_120(self, dialogs):
        print(f'send 120: {dialogs}')


    def send_121(self, messages):
        print(f'send 121: {messages}')