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
SessionFactory = sessionmaker(bind=engine)


# 用户表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), unique=True, nullable=False)
    nikename = Column(String(10), unique=True)
    pwd = Column(String(20), nullable=False)
    email = Column(String(30), unique=True)
    mobile_number = Column(String(11), unique=True, nullable=False)
    person_info = Column(Text)
    avatar = Column(String(100))
    register_time = Column(DateTime, index=True, default=datetime.now(), nullable=False)
    message = relationship("Message", backref='users')


# message
class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    leave_msg_time = Column(DateTime, index=True, default=datetime.now(), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))


# crete all tables
def create_table():
    Base.metadata.create_all(engine)  # 创建这个数据表


# drop all tables
def drop_table():
    Base.metadata.drop_all(engine)  # 删除这个数据表


# connect database
def connect_db():
    # 去连接池获取一个连接
    session = SessionFactory()
    return session


if __name__ == '__main__':
    # create_table()
    session = connect_db()
    # ret = session.query(Users).all()  # 列表类型,里面存储对象
    # ret = session.query(Users).filter(Users.mobile_number==18512152005).count()  # 列表中的对象
    # print(ret)
    # drop_table()
