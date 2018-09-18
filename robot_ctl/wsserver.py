# -*- coding:utf8 -*-
import datetime
import threading
import time

from flask import Flask, Blueprint
from flask_sockets import Sockets

ws_blueprint = Blueprint(r'ws', __name__)

wss = {}

def init_ws(app):
    sockets = Sockets(app)
    sockets.register_blueprint(ws_blueprint, url_prefix=r'/')


@ws_blueprint.route('/echo')
def echo_socket(ws):
    def echo(nt):
        while not ws.closed:
            now = datetime.datetime.now().isoformat() + 'Z'
            ws.send(now)  # 发送数据
            time.sleep(1)

    t = threading.Thread(target=echo, args=('',))
    t.daemon = True
    t.start()


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    app = Flask(__name__)
    init_ws(app)
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
