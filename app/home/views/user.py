# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午2:03
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : user.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template
from app.models import connect_db


@home_bp.route('/v1/register')
def register():
    
    return '注册成功！'
