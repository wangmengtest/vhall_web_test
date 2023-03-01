#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.sangfor.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_sangfor_api")
testObj.setDbSection("dev_sangfor_db")

feAuthData = {
    "username":"18782931195",
    "password":"123456",
    "phone": "18782931195",
    "code": "111111",
    "is_console": 1,
    "nickname":"18782931195",
    "is_role":0,
    "type" : 2,
    "from" : "js",
}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
