# coding=utf-8
import datetime
import json

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from robot_ctl.logger import getLogger
from robot_ctl.model import QQ, User, Wx, get_db_session

logger = getLogger(__name__)

# SQLAlchemy orm
Base = declarative_base()


# for QQ
# SQLAlchemy orm
# retrieve
def get_qq_mapped(qq_no):
    try:
        ret = QQ.query.filter_by(qq_no=qq_no).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for QQ
# SQLAlchemy orm
# delete
def del_qq_mapped(qq_no):
    try:
        s = get_db_session()
        ret = QQ.query.filter_by(qq_no=qq_no).first()
        s.delete(ret)
        s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# delete
def del_qqlist_mapped(qq_nos):
    global s
    try:
        s = get_db_session()
        filters = {
            QQ.qq_no.in_(json.loads(qq_nos))
        }
        ret = QQ.query.filter(QQ.qq_no.in_(json.loads(qq_nos))).all()
        # Object '<QQ at 0x64affd0>' is already attached to session '6' (this is '5')
        for item in ret:
            s.delete(item)
        s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# update
def put_qq_mapped(qq_json):
    global s
    try:
        qq_obj = json.loads(qq_json)
        s = get_db_session()
        ret = QQ.query.filter_by(id=qq_obj['id']).first()
        if ret is not None:
            modified = False
            if qq_obj['qq_no'] is not None:
                ret.qq_no = qq_obj['qq_no']
                modified = True
            if qq_obj['password'] is not None:
                ret.password = qq_obj['password']
                modified = True
            if modified:
                ret.update_time = datetime.datetime.now()
        s.add(ret)
        s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# create
def post_qq_mapped(qq_json):
    global s
    try:
        s = get_db_session()
        now = datetime.datetime.now()
        qq_obj = json.loads(qq_json)
        qq = QQ(0, qq_obj['qq_no'], qq_obj['password'], now, now)
        s.add(qq)
        ret = s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# retrieve list
def get_qq_nos_mapped(nos):
    global s
    try:
        ret = QQ.query.filter(QQ.qq_no.in_(json.loads(nos))).all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for QQ
# SQLAlchemy orm
# retrieve list
def get_qq_list_mapped():
    try:
        ret = QQ.query.all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for QQ
# SQLAlchemy orm
# retrieve page
def get_qq_page(page, size):
    try:
        p = int(page)
        l = int(size)
        ret = QQ.query.paginate(p, l, False)
        pages = ret.pages
        current = ret.page
        return ret.items, current, pages
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for WX
# SQLAlchemy orm
# retrieve
def get_wx_mapped(wx_no):
    try:
        ret = Wx.query.filter_by(wx_no=wx_no).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for WX
# SQLAlchemy orm
# delete
def del_wx_mapped(wx_no):
    global s
    try:
        s = get_db_session()
        ret = Wx.query.filter_by(wx_no=wx_no).first()
        s.delete(ret)
        s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# update
def put_wx_mapped(wx_json):
    global s
    try:
        wx_obj = json.loads(wx_json)
        s = get_db_session()
        ret = s.query(Wx).filter_by(id=wx_obj['id']).first()
        if ret is not None:
            modified = False
            if wx_obj['wx_no'] is not None:
                ret.wx_no = wx_obj['wx_no']
                modified = True
            if wx_obj['wx_name'] is not None:
                ret.wx_name = wx_obj['wx_name']
                modified = True
            if wx_obj['password'] is not None:
                ret.password = wx_obj['password']
                modified = True
            if modified:
                ret.update_time = datetime.datetime.now()
        s.add(ret)
        s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# create
def post_wx_mapped(wx_json):
    global s
    try:
        wx_obj = json.loads(wx_json)
        s = get_db_session()
        now = datetime.datetime.now()
        wx = Wx(-1, wx_obj['qq_no'], wx_obj['password'], now, now)
        s.add(wx)
        ret = s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# retrieve list
def get_wx_list_mapped():
    try:
        ret = Wx.query.all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


# for WX
# SQLAlchemy orm
# retrieve page
def get_wx_page(page, size):
    try:
        p = int(page)
        l = int(size)
        ret = Wx.query.paginate(p, l, False)
        pages = ret.pages
        current = ret.page
        return ret.items, current, pages
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None


def get_user_session(user_id):
    try:
        ret = User.query.filter_by(username=user_id).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None