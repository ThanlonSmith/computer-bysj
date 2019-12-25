# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午3:46
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : about_website.py
# @Software: PyCharm
from .. import home_bp
from flask import render_template


@home_bp.route('/v1/contact-us')
def contact_us():
    return render_template('/home/contact_us.html')
