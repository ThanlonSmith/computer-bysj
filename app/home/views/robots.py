# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 上午12:20
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : robots.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template


@home_bp.route('/robots.txt')
def robots():
    return render_template('robots.txt')
