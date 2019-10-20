# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午1:45
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

home_bp = Blueprint('home', __name__)
from .views import user
