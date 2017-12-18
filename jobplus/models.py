#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/12/18/0017 21:50
# @Author  : Hython.com
# @File    : models.py
"""
jobplus.models.py
实现了所有的model类及相应的序列化类
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#todo 数据库表模型
class Person(db.Model):
    """应聘者类"""
    __tablename__ = 'person'
    pass