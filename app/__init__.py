# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午12:44
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask

from app.admin import admin_bp
from app.home import home_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)
    return app
