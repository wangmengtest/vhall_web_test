#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_csces_api")
testObj.setDbSection("dev_csces_db")

feAuthData = {
    "username": "liuweifei",
    "password": "liuyh@140203",
}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
