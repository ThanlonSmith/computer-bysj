# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 下午5:31
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : mall.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template
@home_bp.route('/v1/mall')
def mall():
    return render_template('/home/mall.html')