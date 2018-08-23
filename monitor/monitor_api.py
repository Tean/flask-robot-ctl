# coding=utf-8
import random
import time

from flask import jsonify
from flask_restful import Resource, abort
from flask_restful.reqparse import RequestParser


# http://www.flaskapi.org/
# https://www.fullstackpython.com/api-creation.html
# 使用Flask-RESTful构建REST API
# http://flask-restful.readthedocs.io/en/latest/
# https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
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

class Act1(Resource):
    def get(self, id):
        return find(id)

    def post(self, id):
        db[id] = parser.parse_args()
        return '', 202


class Act2(Resource):
    def get(self, id):
        return find(id)


class Act3(Resource):
    def get(self, id):
        return find(id)
