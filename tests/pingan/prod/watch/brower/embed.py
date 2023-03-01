#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.watch.room import *
from utils.config_util import configUtil

testObj = Room("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
testObj.setSignRequest()

result = testObj.roomInfo({
    "third_id": 111,
    "nickname": 222,
})
