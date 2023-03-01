#!/usr/bin/env python
# encoding:utf8

from app.preview.herbalife.master.auth import *
from utils.random_util import randomUtil

testObj = Auth("test_herbalife_api")
# testObj = Auth("dev_herbalife_api")
testObj.setDbSection("dev_common_db")


doLogin = {
    "phone": 18510248667,
    "code": 123456,
    "user_type": 1
}
testObj.doLogin(doLogin, "console_token")
