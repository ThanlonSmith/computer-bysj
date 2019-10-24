# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 下午3:25
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : feedback.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template


@home_bp.route('/v1/feedback')
def feedback():
    return render_template('/home/feedback.html')
