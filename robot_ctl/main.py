import logging

from flask import Flask
import sys

# sys.path.append('D:\\Projects\\GitHub\\flask-robot-ctl')
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

sys.path.append('..')

from robot_ctl import api, model, login_manager, wsserver, wsioserver
from robot_ctl.page import robot_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9CNa0BvE@47.107.53.36:3306/robot_ctl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'aHR0cDovL3d3dy53YW5kYS5jbi8='

app.register_blueprint(robot_blueprint, static_folder='static')

# app.config['SECRET_KEY'] = 'secret!'
app.config['SECRET_KEY'] = 'secret!'

model.init_app(app)

api.init_api(app)

login_manager.init_app(app)

sio = wsioserver.init_wsio(app)

if __name__ == '__main__':
    # print(type(flask_db.get_user('admin')))
    # print(flask_db.get_user('admin'))

    # server = pywsgi.WSGIServer(('', 9000), app, handler_class=WebSocketHandler)
    # server.serve_forever()
    # app.run(port=9000)
    app.debug = False
    print('main start up')
    sio.run(app, port=8081)
