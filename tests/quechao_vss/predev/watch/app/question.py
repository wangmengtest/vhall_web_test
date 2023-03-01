#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.watch.question import *
from utils.config_util import configUtil

testObj = Question("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()