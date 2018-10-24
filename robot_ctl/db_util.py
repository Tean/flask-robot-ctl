# coding=utf-8
import datetime
import json

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from robot_ctl.logger import getLogger
from robot_ctl.model import QQ, User, Wx

config = {
    'host': 'localhost',
    'user': 'tester',
    'password': '1234',
    'port': 3306,
    'database': 'robot_ctl',
    'charset': 'utf8'
}
config['host'] = '47.107.53.36'
config['user'] = 'root'
config['password'] = '9CNa0BvE'

# db_url = 'mysql+pymysql://tester:1234@localhost:3306/robot_ctl'
db_url = 'mysql+pymysql://root:9CNa0BvE@47.107.53.36:3306/robot_ctl'

select_qq_list = 'select * from qq_list'
select_qq_by_no = 'select * from qq_list where qq_no = %s limit 1'

logger = getLogger(__name__)


# get database connection using mysql.connector
def get_connection():
    try:
        conn = pymysql.connect(config['host'], config['user'], config['password'], config['database'])
        return conn
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None

        # get database connection


# get user by user_id
def get_qq(qq_number):
    global cursor, conn
    try:
        conn = get_connection()
        logger.debug("conn is %s" % conn)
        if conn:
            cursor = conn.cursor()
            cursor.execute(select_qq_by_no, (qq_number,))
            result = cursor.fetchall()
            logger.debug("conn is %s" % conn)
            return result
        else:
            logger.debug("conn is %s" % conn)
        return None
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        cursor.close()
        conn.close()


def get_qq_list():
    global cursor, conn
    try:
        conn = get_connection()
        logger.debug("conn is %s" % conn)
        if conn:
            cursor = conn.cursor()
            cursor.execute(select_qq_list)
            result = cursor.fetchall()
            logger.debug("conn is %s" % conn)
            return result
        else:
            logger.debug("conn is %s" % conn)
        return None
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
        return None
    finally:
        cursor.close()
        conn.close()


# SQLAlchemy orm
Base = declarative_base()


# for QQ
# SQLAlchemy orm
# retrieve
def get_qq_mapped(qq_no):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(QQ).filter_by(qq_no=qq_no).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# delete
def del_qq_mapped(qq_no):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(QQ).filter_by(qq_no=qq_no).first()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        qq_obj = json.loads(qq_json)
        s = session()
        ret = s.query(QQ).filter_by(id=qq_obj['id']).first()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        qq_obj = json.loads(qq_json)
        s = session()
        now = datetime.datetime.now()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = QQ.query.filter(QQ.qq_no.in_(json.loads(nos))).all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# retrieve list
def get_qq_list_mapped():
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(QQ).all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


# for QQ
# SQLAlchemy orm
# retrieve page
def get_qq_page(page, size):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        # ret = s.query(QQ).all();
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
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# retrieve
def get_wx_mapped(wx_no):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(Wx).filter_by(wx_no=wx_no).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# delete
def del_wx_mapped(wx_no):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(Wx).filter_by(wx_no=wx_no).first()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        wx_obj = json.loads(wx_json)
        s = session()
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
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        wx_obj = json.loads(wx_json)
        s = session()
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
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(Wx).all()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


# for WX
# SQLAlchemy orm
# retrieve page
def get_wx_page(page, size):
    global s
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        # ret = s.query(QQ).all();
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
    finally:
        s.close()


def get_user_session(user_id):
    try:
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(User).filter_by(username=user_id).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None


# get connection session
def get_connection_session(url):
    global s
    try:
        engine = create_engine(url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        return s
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None
    finally:
        s.close()


# get connection using url
def get_connection_with_url(url):
    try:
        engine = create_engine(url, echo=True)
        conn = engine.connect()
        return conn
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None


if __name__ == '__main__':
    # print(get_qq('233'))
    print(get_qq_mapped('233'))
