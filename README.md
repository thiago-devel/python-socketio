# python-socket.io

Socket.io example:
https://github.com/miguelgrinberg/python-socketio/blob/master/examples/server/aiohttp/app.py
https://github.com/miguelgrinberg/python-socketio/blob/master/examples/server/aiohttp/app.html
https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/aiohttp

Socket.io python docs
https://python-socketio.readthedocs.io/en/latest/intro.html#server-examples


set APP_SETTINGS=config.DevelopmentConfig



mkvirtualenv python-socketio

workon python-socketio

set APP_SETTINGS=config.DevelopmentConfig

deactivate


python -m pip install flask-socketio eventlet
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt


references:

https://github.com/miguelgrinberg/Flask-SocketIO
https://raw.githubusercontent.com/miguelgrinberg/Flask-SocketIO/master/example/app.py
https://raw.githubusercontent.com/miguelgrinberg/Flask-SocketIO/master/example/templates/index.html
https://flask-socketio.readthedocs.io/en/latest/
https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/
https://github.com/shanealynn/async_flask
http://logan.tw/posts/2016/01/16/flask-and-socketio/
https://realpython.com/python-concurrency/
https://realpython.com/lessons/multiprocessing-module/