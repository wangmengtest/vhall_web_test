#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.openapi.inav import *
from utils.config_util import configUtil

testObj = Inav("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
testObj.setSignRequest()

result = testObj.postNoAppId('openapi/inav/get-account',{
    "thirdId": 111,
    "nickname": 222,
})
