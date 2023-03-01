#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.huawei.admin.auth import *

testObj = Auth("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")


feAuthData = {
    "admin_name": "admin",
    "password": "admin123",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
