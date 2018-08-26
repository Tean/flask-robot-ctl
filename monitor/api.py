from flask_restful import Api

from monitor import monitor_api


def init_api(app):
    api = Api(app)
    api.add_resource(monitor_api.MonitorApi, '/api/<id>')
    api.add_resource(monitor_api.Acts, '/api/acts')
    api.add_resource(monitor_api.QQList, '/api/qq/list')
    api.add_resource(monitor_api.QQByNo, '/api/qq/<qq_no>')
    api.add_resource(monitor_api.QQAdd, '/api/qq')
    api.add_resource(monitor_api.QQPage, '/api/qq/page/<page>/size/<size>')
    api.add_resource(monitor_api.Act3, '/api/wx/<id>')
