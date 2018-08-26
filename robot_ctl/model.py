from datetime import date, datetime
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


def init_app(app):
    return db.init_app(app)


class QQ(db.Model):
    __tablename__ = 'qq_list'

    id = Column('id', Integer, primary_key=True)
    qq_no = Column('qq_no', String(20))
    password = Column('password', String(128))
    create_time = Column('create_time', String(128))
    update_time = Column('update_time', String(128))

    def __init__(self, id, qq_no, password, create_time, update_time):
        self.id = id
        self.qq_no = qq_no
        self.password = password
        self.create_time = create_time
        self.update_time = update_time

    def __repr__(self):
        return '<id is %s, username is %s, password is %s, create time is %s, update time is %s>' % (
            self.id, self.qq_no, self.password, self.create_time, self.update_time)


class QQEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, QQ):
            # return obj.id, obj.qq_no, obj.password, obj.create_time, obj.update_time
            return {'id': obj.id, 'qq_no': obj.qq_no, 'password': obj.password, 'create_time': obj.create_time,
                    'update_time': obj.update_time}
        else:
            return json.JSONEncoder.default(self, obj)


class User(db.Model):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(128))
    email = Column('email', String(128))
    password = Column('password', String(128))
    create_time = Column('create_time', String(128))
    update_time = Column('update_time', String(128))

    def __init__(self, id, username, email, password, create_time, update_time):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.create_time = create_time
        self.update_time = update_time

    def __repr__(self):
        return '<id is %s, username is %s, password is %s, email is %s, create time is %s, update time is %s>' % (
            self.id, self.username, self.password, self.email, self.create_time, self.update_time)
