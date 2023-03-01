#!/usr/bin/env python
# encoding:utf8

from app.preview.vhall_app_java.master.auth import *
from utils.random_util import randomUtil

testObj = Auth("dev_vhall_app_java_api")
testObj.setDbSection("dev_vhall_app_java_db")


doLogin = {
    "phone": 18510248667,
    "code": 123456,
    "user_type": 1
}
testObj.doLogin(doLogin, "console_token")
