# coding=utf-8
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import monitor_logger
import monitor_user

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': 3306,
    'database': 'robot_ctl',
    'charset': 'utf8'
}
user_orm_url = 'mysql+pymysql://tester:1234@localhost:3306/robot_ctl'

user_sql = 'select * from user where username = %s limit 1'
logger = monitor_logger.get_logger(__name__)


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
def get_user(user_id):
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(user_sql, (user_id,))
            result = cursor.fetchall()
            logger.debug("conn is %s" % conn)
            return result
        else:
            logger.debug("conn is %s" % conn)
            return None
        logger.debug("conn is %s" % conn)
        return None
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None
    finally:
        cursor.close()
        conn.close()


# SQLAlchemy orm
Base = declarative_base()


# for login
# SQLAlchemy orm
def get_user_session(user_id):
    try:
        engine = create_engine(user_orm_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        s = session()
        ret = s.query(monitor_user.User).filter_by(username=user_id).first()
        return ret
    except Exception as e:
        logger.debug("Exception is %s" % e)
        return None


# get connection session
def get_connection_session(url):
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
    print(get_user_session('admin'))
    print(get_user('admin'))
