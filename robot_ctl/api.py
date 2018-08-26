# coding=utf-8
import json
import random
import time

from flask import jsonify, request
from flask_restful import Api, Resource

from robot_ctl.db_util import get_qq_list_mapped, get_qq_page, get_qq_mapped, del_qq_mapped, post_qq_mapped, \
    put_qq_mapped
from robot_ctl.model import QQEncoder


def init_api(app):
    api = Api(app)
    api.add_resource(ApiId, '/api/<id>')
    api.add_resource(ApiActs, '/api/acts')
    api.add_resource(QQList, '/api/qq/list')
    api.add_resource(QQByNo, '/api/qq/<qq_no>')
    api.add_resource(QQAdd, '/api/qq')
    api.add_resource(QQPage, '/api/qq/page/<page>/size/<size>')
    api.add_resource(Act3, '/api/wx/<id>')


class ApiId(Resource):
    @staticmethod
    def get(id):
        t = time.time()
        # nowTime = lambda: int(round(t * 1000))
        # print (nowTime())
        return jsonify({'id': id, 'value': random.random(), 'timestamp': t})


class ApiActs(Resource):
    def get(self):
        return '', 202


class QQList(Resource):
    def get(self):
        qqs = get_qq_list_mapped()
        return jsonify(json.dumps(qqs, cls=QQEncoder))

    def post(self, id):
        return '', 202


class QQPage(Resource):
    def get(self, page, size=10):
        qqs = get_qq_page(page, size)
        return jsonify(json.dumps(qqs, cls=QQEncoder))


class QQByNo(Resource):
    def get(self, qq_no):
        qq = get_qq_mapped(qq_no)
        return jsonify(json.dumps(qq, cls=QQEncoder))

    def delete(self, qq_no):
        id = del_qq_mapped(qq_no)
        return jsonify(id)


class QQAdd(Resource):
    def post(self):
        json = request.json
        ret = post_qq_mapped(json)
        return jsonify(ret)

    def put(self):
        json = request.json
        ret = put_qq_mapped(json)
        return jsonify(ret)


class Act3(Resource):
    def get(self, id):
        pass
