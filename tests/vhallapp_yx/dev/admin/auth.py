#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.vhallapp.admin.auth import *

testObj = Auth("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")


feAuthData = {
    "admin_name": "admin",
    "password": "admin123",
    "from": "js"
}
testObj.doLogin(feAuthData, "admin_token")
