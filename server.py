from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import sys
sys.path.insert(1, './app')

from PH import PH
from connector import Connector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,  cors_allowed_origins='*')

ph = PH()
conn = Connector()


@app.route('/login')
@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('proto20')
def proto_20(mproto_query):
    answer = ph.handle(mproto_query)
    print('proto 20')
    emit('proto20', answer)


@socketio.on('proto21')
def proto_21(mproto_query):
    answer = ph.handle(mproto_query)
    print('proto 21')
    emit('proto21', answer)


if __name__ == "__main__":
    conn.connect()
    socketio.run(app, debug=True)

