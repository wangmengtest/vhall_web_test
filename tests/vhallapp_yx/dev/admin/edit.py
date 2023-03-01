#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.vhallapp.admin.admin import *

testObj = Admin("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})

feAuthData = {
    "admin_name": "admin",
    "admin_id":1,
    "email": "test001@vhall.com",
    "password": "admin123",
    "confirm_password": "admin123",
    "role_id":1,
    "from": "js"
}
testObj.edit(feAuthData)
