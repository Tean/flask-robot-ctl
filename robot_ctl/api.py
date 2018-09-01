# coding=utf-8
import httplib
import json
import random
import time

from flask import jsonify, request
from flask_restful import Api, Resource, reqparse

from robot_ctl.db_util import get_qq_list_mapped, get_qq_page, get_qq_mapped, del_qq_mapped, post_qq_mapped, \
    put_qq_mapped, get_wx_list_mapped, get_wx_page, get_wx_mapped, del_wx_mapped, post_wx_mapped, put_wx_mapped, \
    del_qqlist_mapped, get_qq_nos_mapped
from robot_ctl.logger import getLogger
from robot_ctl.model import QQEncoder, Generator

logger = getLogger(__name__)


class ApiRequest:
    def get(self, url):
        http_client = httplib.HTTPConnection(url, timeout=20)
        http_client.request('GET', '')
        r = http_client.getresponse()
        return r.read()


def init_api(app):
    api = Api(app)
    api.add_resource(ApiId, '/api/<id>')
    api.add_resource(ApiActs, '/api/acts')
    api.add_resource(QQList, '/api/qq/list')
    api.add_resource(QQListParam, '/api/qq/list/<nos>')
    api.add_resource(QQByNo, '/api/qq/<qq_no>')
    api.add_resource(QQAdd, '/api/qq')
    api.add_resource(QQPage, '/api/qq/page/<index>')
    api.add_resource(WxList, '/api/wx/list')
    api.add_resource(WxByNo, '/api/wx/<wx_no>')
    api.add_resource(WxAdd, '/api/wx')
    api.add_resource(WxPage, '/api/wx/page/<index>')


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
        return Generator.makeQQList(qqs)


class QQListParam(Resource):
    def get(self, nos):
        qqs = get_qq_nos_mapped(nos)
        return Generator.makeQQList(qqs)

    def delete(self, nos):
        # ret = del_qqlist_mapped(nos)
        nolist = json.loads(nos);
        # unbound method delete() must be called with QQByNo instance as first argument (got int instance instead)
        for no in nolist:
            QQByNo.delete(no)
        return 200, ''


class QQPage(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('size', type=int, required=False, default=10)

    def get(self, index):
        data = self.parser.parse_args()
        size = data.get('size')
        qqs = get_qq_page(index, size)
        qqlist = qqs[0] if qqs is not None and qqs[0] is not None else []
        index = qqs[1] if qqs is not None and qqs[1] is not None else 1
        pages = qqs[2] if qqs is not None and qqs[2] is not None else 0
        lists = Generator.makeQQList(qqlist)
        ret = {'index': index, 'pages': pages, 'items': lists}
        return ret


class QQByNo(Resource):
    def get(self, qq_no):
        qq = get_qq_mapped(qq_no)
        return Generator.makeQQ(qq)

    def delete(self, qq_no):
        id = del_qq_mapped(qq_no)
        return jsonify(id)


class QQAdd(Resource):
    def post(self):
        jsn = request.json
        if jsn is None:
            ret = request.values.to_dict()['qq']
        else:
            ret = jsn

        ret = post_qq_mapped(ret)
        return jsonify(ret)

    def put(self):
        json = request.json
        ret = put_qq_mapped(json)
        return jsonify(ret)


class WxList(Resource):
    def get(self):
        wxs = get_wx_list_mapped()
        return jsonify(json.dumps(wxs))

    def post(self, id):
        return '', 202


class WxPage(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('size', type=int, required=False, default=10)

    def get(self, index):
        data = self.parser.parse_args()
        size = data.get('size')
        wxs = get_wx_page(index, size)
        wxlist = wxs[0] if wxs is not None and wxs[0] is not None else []
        index = wxs[1] if wxs is not None and wxs[1] is not None else 1
        pages = wxs[2] if wxs is not None and wxs[2] is not None else 0
        lists = Generator.makeWxList(wxlist)
        ret = {'index': index, 'pages': pages, 'items': lists}
        return ret


class WxByNo(Resource):
    def get(self, wx_no):
        wx = get_wx_mapped(wx_no)
        return Generator.makeWx(wx)

    def delete(self, wx_no):
        id = del_wx_mapped(wx_no)
        return jsonify(id)


class WxAdd(Resource):
    def post(self):
        jsn = request.json
        ret = post_wx_mapped(jsn)
        return jsonify(ret)

    def put(self):
        json = request.json
        ret = put_wx_mapped(json)
        return jsonify(ret)
