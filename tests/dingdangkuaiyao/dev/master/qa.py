#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.master.question import *
from utils.config_util import configUtil

testObj = Question("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})