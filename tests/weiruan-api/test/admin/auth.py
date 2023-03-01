#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.admin.auth import *

testObj = Auth("test_pingan_api")
testObj.setDbSection("dev_pingan_db")


feAuthData = {
    "admin_name": "admin",
    "password": "123456",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
