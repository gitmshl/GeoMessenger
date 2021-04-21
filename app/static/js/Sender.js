class Sender{

    static sio = null;

    static setSio(sio){
        this.sio = sio;
    }

    static send_20(){
        console.log("Sender.send_20()");
        this.sio.emit('proto20', {'code': 20});
    }

    static send_21(dialog_id){
        console.log("Sender.send_21");
        this.sio.emit('proto21', {'code': 21, 'dialog_id': dialog_id});
    }

}