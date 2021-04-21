class PH{

    static handle(obj){
        let code = obj.code;
        switch (code) {
            case 120: this.handle_120(obj.dialogs); break;
            case 121: this.handle_121(obj); break;
            default:
                console.log(obj)
                alert('Пришел запрос с неизвестным кодом!!!');
        }
    }

    static handle_120(dialogs){
        console.log('handle 120');
        if (!SST.checkWaitingForResponse(120)) return;
        SST.setResponse(120);
        Timer.clearTimer_20();
        Painter.AddInDialogList(dialogs);
        Painter.showDialogList();
        SST.setHandshake(true);
    }

    static handle_121(obj){
        if (!SST.checkWaitingForResponse(121)) return;
        SST.setResponse(121);
        Timer.clearTimer_21();
        console.log('handle 121');
        let messages = obj.messages;
        let lastMsgInf = obj.lastMsgInf;
        console.log('handle 121');
        console.log(messages);
        console.log(lastMsgInf);
        
        Painter.AddInDialog(lastMsgInf, messages);

        /* Производим проверку того, нужно ли отправлять запрос 1 на сервер */
        /*
        let my_id = SST.getId();
        let from_user_id = data.lastMsgInf.from_user_id;
        if (my_id != from_user_id){
            let last_msg_time = new Date(data.lastMsgInf.last_msg_time);
            let my_last_reading_time = new Date(data.lastMsgInf.my_last_reading_time);
            if (last_msg_time >= my_last_reading_time)
                Sender.send_1();
        }*/

    }


}