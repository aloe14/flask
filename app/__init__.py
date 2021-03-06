#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2020/6/3 14:14
__author__ = 'Aloe'


from flask import Flask
# 导入配置文件
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
# 添加配置信息
app.config.from_object(Config)
# 建立数据库关系
db = SQLAlchemy(app)
from app import routes, models
# 绑定app和数据库，以便进行操作
migrate = Migrate(app, db)


