# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午12:38
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : manage.py
# @Software: PyCharm
from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
