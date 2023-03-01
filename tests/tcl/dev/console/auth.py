#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.tcl.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_tcl_api")
testObj.setDbSection("dev_tcl_db")

feAuthData = {
    "username": "tcl123",
    "password": "tcl123",
}
testObj.doLogin(feAuthData, "console_token")

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
