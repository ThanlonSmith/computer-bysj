# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午2:03
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : user.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template, request, session
from app.models import connect_db
from random import randint
import requests


@home_bp.route('/v1/send_code', methods=['GET', 'POST'])
def send_code():
    random_verify_code = str(randint(100000, 999999))
    session['random_verify_code'] = random_verify_code
    # print(session['random_verify_code'],type(session['random_verify_code']))
    mobile_number = request.form.get('mobile_number')
    # print(mobile_number)
    req_url = "http://api.feige.ee/SmsService/Send"
    data = {"Account": "18937693205", "Pwd": "61a8ea729e25f1cf745066d33",
            "Content": "验证码:" + random_verify_code + "。此验证码仅用于校验身份以注册/登录https://bysj39.com，10分钟内有效。",
            "Mobile": mobile_number, "SignId": 106861}
    response = requests.post(req_url, data=data)
    # print(response.content)
    return 'ok'


@home_bp.route('/v1/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        verify_code = request.form.get('verify_code')
        # print(verify_code, session['random_verify_code'])
        if verify_code != session['random_verify_code']:
            return '手机验证码输入错误！'
        name = request.form.get('name')
        mobile_number = request.form.get('mobile_number')
        pwd = request.form.get('pwd')
        return 'ok'  # 对应ajax中的data
