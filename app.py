#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/12/17/0017 21:50
# @Author  : Hython.com
# @File    : app.py
"""
app.py
jobplus应用入口文件
"""
from jobplus.app import create_app
from jobplus.models import db


app = create_app()

@app.cli.command()
#todo 输出app中定义的所有路由
def routes():
    """输出app中定义的所有路由"""
    pass

@app.cli.command()
def init_db():
    """初始化数据库"""
    db.create_all()
    print("sqlite3 database file is %s" % app.config['SQLALCHEMY_DATABASE_URI'])