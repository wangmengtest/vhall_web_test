#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")

feAuthData = {
    "phone": "18519184446",
    "code": "111111",
    "is_console": 1,
    "nickname":"111111",
    "is_role":0,
    "type" : 1,

}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
