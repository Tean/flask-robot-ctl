import json
from datetime import datetime, date

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# http://docs.sqlalchemy.org/en/latest/orm/mapping_columns.html
class QQ(Base):
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
