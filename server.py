from flask import Flask, request, render_template, session, url_for, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room

from app import ph, conn, app, socketio
from custom_exceptions import DBConnectionException
from DBHandler import DBHandler


@app.route('/login')
@app.route('/')
def login():
    if 'user_id' in session:
        return redirect(url_for('messenger'))
    return render_template('index.html')


@app.route('/aut', methods=['POST'])
def aut():
    user_login = request.args.get('login')
    user_password = request.args.get('password')
    if user_login and user_password:
        try:
            res = ph._getIdAndPasswordByLogin(user_login)
            if not res:
                return {'status': 'incorrect'}
            id, password = res
        except DBConnectionException:
            return {'status': 'fail'}

        if user_password != password:
            return {'status': 'incorrect'}
        
        session['user_login'] = user_login
        session['user_id'] = id
        return {'status': 'success', 'id': id}
    else:
        return {'status': 'incorrect'}


@app.route('/messenger')
def messenger():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('messenger.html', user_login=session['user_login'], user_id=session['user_id'], rooms=['room1', 'room2'])


@socketio.on('proto20')
def proto_20(mproto_query):
    answer = ph.handle(mproto_query, session['user_id'])
    print('proto 20')
    emit('proto20', answer)


@socketio.on('proto21')
def proto_21(mproto_query):
    answer = ph.handle(mproto_query, session['user_id'])
    print('proto 21')
    emit('proto21', answer)


if __name__ == "__main__":
    conn.connect()
    socketio.run(app, debug=True)

