#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.pingan.admin.auth import *

testObj = Auth("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")


feAuthData = {
    "admin_name": "admin",
    "password": "123456",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
