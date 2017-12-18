#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/12/18/0018 0:09
# @Author  : Hython.com
# @File    : config.py jobplus的配置文件
import os


class DevConfig:
    """开发环境配置信息"""

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True


class ProductConfig:
    """生产环境配置信息"""

    DEBUG = False

    # sqlite 数据库文件路径
    path = os.path.join(os.getcwd(), 'jobplus5.db').replace('\\', '/')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % path