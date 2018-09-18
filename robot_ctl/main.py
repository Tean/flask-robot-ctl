import logging

from flask import Flask
import sys

# sys.path.append('D:\\Projects\\GitHub\\flask-robot-ctl')
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

sys.path.append('..\\..\\flask-robot-ctl')
sys.path.append('../../flask-robot-ctl')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] - %(name)s:[%(lineno)d] - %(levelname)s - %(message)s'
)

from robot_ctl import api, model, login_manager, wsserver, wsioserver
from robot_ctl.page import robot_blueprint

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_PATH'] = 'upload'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tester:1234@localhost:3306/robot_ctl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOADS_DEFAULT_DEST'] = app.config['UPLOAD_PATH']
app.config['UPLOADS_DEFAULT_URL'] = 'http://127.0.0.1:9000/'

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
    # app.debug = True
    sio.run(app, port=9000, debug=False)
