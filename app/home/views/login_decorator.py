# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 上午11:48
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : de.py
# @Software: PyCharm
from functools import wraps
from flask import request, session, redirect, url_for

def user_login_rule(foo):
    @wraps(foo)
    def decorated_function(*args, **kwargs):
        if 'name' not in session:  # if not session.get('user_info'):
            return redirect(url_for('home_bp.index', next=request.url))
        return foo(*args, **kwargs)

    return decorated_function
