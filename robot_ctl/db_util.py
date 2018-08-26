# coding=utf-8
import datetime
import json

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from robot_ctl.logger import getLogger
from robot_ctl.model import QQ, User

config = {
    'host': 'localhost',
    'user': 'tester',
    'password': '1234',
    'port': 3306,
    'database': 'robot_ctl',
    'charset': 'utf8'
}

db_url = 'mysql+pymysql://tester:1234@localhost:3306/robot_ctl'

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


# for login
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
        updates = json.dumps(qq_obj)
        ret = s.query(QQ).filter_by(qq_no=qq_obj['qq_no']).first()
        if ret is not None:
            if qq_obj['password'] is not None:
                ret.password = qq_obj['password']
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
        qq = QQ(-1, qq_obj['qq_no'], qq_obj['password'], now, now)
        s.add(qq)
        ret = s.commit()
        return ret.id
    except Exception as e:
        logger.debug("Exception is %s" % e)
        s.rollback()
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


# page
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
        return ret.items
    except Exception as e:
        logger.debug("Exception is %s" % e)
        # s.rollback()
        return None
    finally:
        s.close()


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
