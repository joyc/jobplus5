#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/12/17/0017 21:50
# @Author  : Hython.com
# @File    : app.py
"""
jobplus.app
实现了app创建函数
"""
import os
from flask import Flask

from jobplus.models import db
from jobplus.config import DevConfig, ProductConfig


def create_app():
    """创建并初始化JobPlus App"""
    app = Flask('jobplus')

    # 根据环境加载配置信息
    env = os.environ.get('JOBPLUS_ENV')

    if env in ('pro', 'prod', 'product'):
        app.config.from_object(ProductConfig)
    else:
        app.config.from_object(DevConfig)

    #todo 从环境变量指定文件加载配置信息
    pass

    # 初始化数据库
    db.init_app(app)