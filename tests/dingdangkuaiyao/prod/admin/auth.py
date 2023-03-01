#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.admin.auth import *

testObj = Auth("prod_pingan_api")
testObj.setDbSection("dev_csces_db")


feAuthData = {
    "admin_name": "admin",
    "password": "123456",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
