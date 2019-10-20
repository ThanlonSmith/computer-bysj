# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午1:45
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', )
