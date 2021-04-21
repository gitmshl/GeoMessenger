
$(document).ready( () => {

    let current_room = -1;
    var sio = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    
    SST.init();
    Painter.init();
    Timer.init();
    Sender.setSio(sio);
    UC.req_20();


    sio.on('getMessages', data => {
        insertMessages(data);
    });

    sio.on('message', data => {
        if (current_room != data.room) {console.log('we received a message, but it isn"t so important'); return;}
        insertMessages({'messages': [data]});
    });

    sio.on('proto20', data => {
        console.log('proto20');
        PH.handle(data);
    });

    sio.on('proto21', data => {
        console.log('proto21');
        PH.handle(data);
    });



































    

    /*document.querySelectorAll(".dialog_block").forEach(item => {
        let room_name = item.id.slice(3);
        item.addEventListener("click", event => {
            goTo(room_name);
        });
        sio.emit('join', {'username': username, 'room': room_name});
    });*/


    /*$("#link_to_dialogs").click(event => {
        let Dialog = document.getElementById("Dialog");
        Dialog.style.display = "none";
        document.getElementById("Messages").querySelectorAll(".dialog_history_current_dialog").forEach(item => {
            item.remove();
        });
        document.getElementById("DialogList").style.display = "block";
        current_room = -1;
    });

    function goTo(room){
        document.getElementById("DialogList").style.display = "none";
        let Dialog = document.getElementById("Dialog");
        Dialog.style.display = "block";
        Dialog.getElementsByClassName("sub1_current_dialog")[0].getElementsByTagName("a")[0].innerHTML = room;
        sio.emit('getMessages', {'room' : room});
        current_room = room;
        window.scroll(0, 9999);
        document.getElementById("textar").focus();
    }

    function insertMessages(data){
        let messages = data.messages;
        let root = document.getElementById("Messages");
        console.log(messages);
        messages.forEach(message => {
            let div1 = document.createElement("div");
            div1.className = "dialog_history_current_dialog";
            div1.id = "message_id_" + message.id;
            let div2 = document.createElement("div");
            div2.className = "message_current_dialog";
            let div3 = document.createElement("div");
            div3.id = "photo_space";
            let avatar = document.createElement("img");
            avatar.id = "avat";
            let div4 = document.createElement("div");
            div4.className = "hiddenUserName_current_dialog";
            div4.innerHTML = message.username;
            let p = document.createElement("p");
            p.className = "message_text_current_dialog";
            p.innerText = message.msg;
            div1.appendChild(div2);
            div2.appendChild(div3);
            div2.appendChild(p);
            div3.appendChild(avatar);
            div3.appendChild(div4);
            root.appendChild(div1);
        });
        document.getElementById("textar").value = "";
        window.scroll(0, 9999);
        console.log("111");
        document.getElementById("textar").focus();
    }*/


















});