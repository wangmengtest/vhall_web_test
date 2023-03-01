#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.vhallapp.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "type":1,
    "username": "liuweifei",
    "nick_name": "ceshi",
    "phone":"18519184449",
    "password": "liuyh@140203",
}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
