#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
feAuthData = {
    "username": "test001",
    "phone": "15210207735",
    "dept":"1001A1100000009THVWW",
    "org":"0001A110000000002ZK4",
    'from':'js'
}
testObj.testCreate(feAuthData)
