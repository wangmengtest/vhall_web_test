#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.admin.auth import *

testObj = Auth("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")


feAuthData = {
    "admin_name": "admin",
    "password": "123456",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
