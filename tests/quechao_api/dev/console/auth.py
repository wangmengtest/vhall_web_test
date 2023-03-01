#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_quechao_api")
testObj.setDbSection("dev_quechao_db")

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
