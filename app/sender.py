
class Sender:
    
    def send_150(self, text):
        msg = f"Ошибка в протоколе: {text}"
        print('send150', msg)

    def send_120(self, dialogs):
        print(f'send 120: {dialogs}')