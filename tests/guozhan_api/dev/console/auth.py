#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.guozhan.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_guozhan_api")
testObj.setDbSection("dev_guozhan_db")

feAuthData = {
    "phone": "18519184446",
    "code": "111111",
    "is_console": 1,
    "nickname":"111111",
    "username":'test',
    "password" : 123456,

}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
