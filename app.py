#!/usr/bin/env python

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from thread import BotThread
from datetime import datetime


import time
from threading import Lock

async_mode = None

app = Flask(__name__)
app.secret_key = os.urandom(48)
app.debug = True

socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('send-msg')
def handle_message(msg):
    emit('show-msg', msg, broadcast=True)
    return None

@socketio.on('send-command')
def handle_send_message(msg):
    print('>>>>>>>>>>>>>')
    print(msg)
    print('<<<<<<<<<<<<<')

    print('>>>>>>>>>>>>>')
    print('criando thread...')
    BetBotThread(socketio)
    print('<<<<<<<<<<<<<')

    now = datetime.now()
    emit('testResponse', 'oi :) Recebi seu comando em: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S")), broadcast=True)
    return None

def run():
    start_time = time.time()
    print('> iniciando bot')
    time.sleep(2)
    duration = time.time() - start_time
    print('> bot encerrado. Gastou [{}] secs.'.format(duration))

if __name__ == '__main__':
    socketio.run(app)