# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午3:46
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : about_website.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template
@home_bp.route('/v1/blueprint')
def blueprint():
    return render_template('/home/blueprint.html')
