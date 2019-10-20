# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午2:03
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : admin.py
# @Software: PyCharm
from .. import admin_bp
from flask import render_template


@admin_bp.route('/')
def index():
    return render_template('admin/index.html')
