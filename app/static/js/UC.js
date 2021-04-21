class UC{
    
    static req_20(){
        console.log("UC.rec_20()");
        Sender.send_20();
        SST.setRequest(20);
        Timer.setTimer_20();
    }

    static goToDialog(dialog_id){
        console.log("UC.goToDialog");
        if (!SST.handshake) return;
        Painter.clearDialog();
        Painter.FromDialogListToDialog(dialog_id);
        SST.setCurrentDialog(dialog_id);
        Sender.send_21(dialog_id);
        SST.setRequest(21);
        Timer.setTimer_21();
    }

    static goToDialogList(){
        console.log("goToDialogList");
        Painter.saveToBuffer(SST.getCurrentDialog(), Painter.getMsg());
        Painter.hideDialog();
        SST.setCurrentDialog(-1);
        Painter.showDialogList();
    }

    static closeConnection(){
        Sender.ws.close();
        document.cookie = "ID=; expires = " + new Date().toUTCString() + ";";
        location.href = "/Messenger_war_exploded/login";
    }

    static logout(){
        console.log("logout");
        Sender.send_40();
    }

    static err_150(){
        console.log("UC.err_150()");
    }

    static err_161(){
        console.log("UC.err_161()");
    }

    static err_timer_10(){
        console.log("err_timer_10");
    }

    static err_timer_11(){
        console.log("err_timer_11");
    }

    static err_timer_20(){
        console.log("err_timer_20");
    }

    static err_timer_21(){
        console.log("err_timer_21");
    }

    static err_timer_30(){
        console.log("err_timer_30");
    }
}