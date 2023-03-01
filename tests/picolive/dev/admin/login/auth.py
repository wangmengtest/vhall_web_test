#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.admin.auth import *

testObj = Auth("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")


feAuthData = {
    "admin_name": "admin",
    "password": "admin123",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
