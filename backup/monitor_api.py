# coding=utf-8
import json
import random
import time

from flask import jsonify, request
from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser

# http://www.flaskapi.org/
# https://www.fullstackpython.com/api-creation.html
# 使用Flask-RESTful构建REST API
# http://flask-restful.readthedocs.io/en/latest/
# https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
from robot_ctl.db_util import get_qq_list_mapped, get_qq_page, get_qq_mapped, del_qq_mapped, post_qq_mapped, put_qq_mapped
from robot_ctl.model import QQEncoder


class MonitorApi(Resource):

    @staticmethod
    def set(self, id):
        pass

    @staticmethod
    def get(id):
        return jsonify({'id': id, 'value': random.random(), 'timestamp': int(time.time())})


parser = RequestParser()

db = {
    '1': {'evt': 'a1'},
    '2': {'evt': 'a2'},
    '3': {'evt': 'a3'},
}


def find(id):
    if id not in db:
        abort(404, message='{} not found in db'.format(id))
    return db[id]


class Acts(Resource):
    def get(self):
        return db


class QQList(Resource):
    def get(self):
        qqs = get_qq_list_mapped()
        return jsonify(json.dumps(qqs, cls=QQEncoder))

    def post(self, id):
        db[id] = parser.parse_args()
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
        return find(id)
