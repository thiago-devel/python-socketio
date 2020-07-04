#import concurrent.futures
#import threading
import time
from threading import Lock

class BotThread():
    

    def __init__(self, socketio):
        self.thread = None
        self.thread_lock = Lock()
        self.socketio = socketio

        with self.thread_lock:
            if self.thread is None:
                self.thread = socketio.start_background_task(self.background_thread)

    def run(self):
        start_time = time.time()
        print('> iniciando bot')
        time.sleep(2)
        duration = time.time() - start_time
        print('> bot encerrado. Gastou [{}] secs.'.format(duration))

    def background_thread(self):
        """Example of how to send server generated events to clients."""
        count = 0
        while True:
            print('to no loop da thread')
            self.socketio.sleep(10)
            count += 1
            self.socketio.emit('thread-test',
                        {'data': 'Server generated event', 'count': count}, broadcast=True)
