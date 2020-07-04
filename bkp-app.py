'''
from aiohttp import web
import socketio
from thread import BetBotThread
from datetime import datetime


sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def send_command(sid, message):
    print("> recebi o comando: {}".format(message))
    BetBotThread()
    await sio.emit('testResponse', "Ok. thread aberta - {}".format(datetime()), room=sid)

@sio.event
async def my_event(sid, message):
    print("message ", message)
    await sio.emit('my_response', {'data': message['data']}, room=sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)

'''

'''
import os
from flask import Flask, render_template
from thread import BetBotThread
from flask_socketio import SocketIO, emit
from thread import BetBotThread
from datetime import datetime
    
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send-command')
async def send_command(message):
    print("> recebi o comando: {}".format(message))
    BetBotThread()
    await emit('testResponse', "Ok. thread aberta - [{}]".format(datetime()))

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)

'''

#!/usr/bin/env python
import os
from threading import Lock
from flask import Flask, render_template, session, request, copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from thread import BetBotThread
from datetime import datetime

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')

@socketio.on('send-command', namespace='/test')
async def send_command(message):
    print("> recebi o comando: {}".format(message))
    BetBotThread()
    await emit('testResponse', "Ok. thread aberta - [{}]".format(datetime()))

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print("> recebi o comando: {}".format(message))
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)