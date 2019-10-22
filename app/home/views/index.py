# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 上午12:59
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : index.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template


@home_bp.route('/')
def index():
    return render_template('/home/index.html')
