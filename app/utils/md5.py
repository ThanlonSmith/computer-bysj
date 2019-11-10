# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 上午8:26
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : md5.py
# @Software: PyCharm
import hashlib
from settings import DevelopmentConfig


def md5(password):
    hash = hashlib.md5(DevelopmentConfig.SALT)
    # hash.update(b'thanlon')
    hash.update(bytes(password, encoding='utf-8'))
    return hash.hexdigest()


if __name__ == "__main__":
    print(md5('123456'))
