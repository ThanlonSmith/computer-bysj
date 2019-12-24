# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午2:03
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : user.py
# @Software: PyCharm
from .. import home_bp
from flask import request, session, redirect, url_for
from app.models import connect_db, Users, UsersLoginLogs
from random import randint
import requests
from sqlalchemy import or_
from app.utils.md5 import md5


@home_bp.route('/v1/send_code', methods=['GET', 'POST'])
def send_code():
    msg = None
    random_verify_code = str(randint(100000, 999999))
    session['random_verify_code'] = random_verify_code
    # print(session['random_verify_code'],type(session['random_verify_code']))
    mobile_number = request.form.get('mobile_number')
    # print(mobile_number)
    req_url = "http://api.feige.ee/SmsService/Send"
    data = {"Account": "18937693205", "Pwd": "61a8ea729e25f1cf745066d33",
            "Content": "验证码:" + random_verify_code + "。您正在使用短信验证码注册登录功能，该验证码仅用于身份校验，请勿泄露给他人使用。",
            "Mobile": mobile_number, "SignId": 106861}
    response = requests.post(req_url, data=data)
    # print(response.content)
    msg = 'ok'
    return msg


@home_bp.route('/v1/register/', methods=['POST'])
def register():
    if request.method == 'POST':
        msg = None
        verify_code = request.form.get('verify_code')
        # print(verify_code, session['random_verify_code'])
        if verify_code != session['random_verify_code']:
            msg = 'verify_code_err'
            return msg
        name = request.form.get('name')
        mobile_number = request.form.get('mobile_number')
        pwd = request.form.get('pwd')
        pwd = md5(pwd)
        session_ = connect_db()
        name_count = ret = session_.query(Users).filter(Users.mobile_number == mobile_number).count()
        if name_count > 0:
            msg = 'name_error'
            return msg
        try:
            user_obj = Users(
                name=name,
                pwd=pwd,
                mobile_number=mobile_number
            )
            session_.add(user_obj)
            session_.commit()
            session_.close()
        except Exception as e:
            msg = 'db_error'
            return msg
        msg = 'ok'
        return msg
    return '不允许Get请求！'


@home_bp.route('/v1/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        msg = None
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        pwd = md5(pwd)
        # print(name, pwd)
        session_ = connect_db()
        user_obj = session_.query(Users).filter(or_(Users.name == name, Users.mobile_number == name),
                                                Users.pwd == pwd)
        count = user_obj.count()
        id = user_obj.first().id
        name = user_obj.first().name
        # print(count, id, name)
        session['id'] = id
        session['name'] = name
        login_logs_obj = UsersLoginLogs(
            ip=request.remote_addr,
            users_id=id,
        )
        session_.add(login_logs_obj)
        session_.commit()
        session_.close()
        if count > 0:
            msg = 'ok'
            return msg
        else:
            msg = 'error'
            return msg
    return '不允许Get请求！'


@home_bp.route('/v1/logout/')
def logout():
    session.pop('name', None)
    return redirect('/')
