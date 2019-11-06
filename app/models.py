# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 下午2:57
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : models.py
# @Software: PyCharm
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://thanlon:39kiku@106.12.115.136:3307/39bysj?charset=utf8',
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 连接池中没有连接最多等待的时间，否则会报错，30s
    pool_recycle=-1,  # 多久之后对线程池中的线程中进行一次连接的回收（重置）-1表示不重置
)


# 用户表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(18), unique=True)
    pwd = Column(String(20))
    email = Column(String(30), unique=True)
    mobile_number = Column(String(11), unique=True)
    person_info = Column(Text)
    avatar = Column(String(100))
    register_time = Column(DateTime, index=True, default=datetime.now())
    message = relationship("Message", backref='users')


# message
class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    leave_msg_time = Column(DateTime, index=True, default=datetime.now())
    users_id = Column(Integer, ForeignKey('users.id'))


# crete all tables
def create_table():
    Base.metadata.create_all(engine)  # 创建这个数据表


# drop all tables
def drop_table():
    Base.metadata.drop_all(engine)  # 删除这个数据表


# connect database
def connect_db():
    SessionFactory = sessionmaker(bind=engine)
    # 去连接池获取一个连接
    session = scoped_session(SessionFactory)
    return session


if __name__ == '__main__':
    create_table()
    # drop_table()
