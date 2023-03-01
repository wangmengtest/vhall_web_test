#!/usr/bin/env python
# encoding:utf8

from app.preview.herbalife.oa.auth import *
from utils.random_util import randomUtil

testObj = Auth("test_herbalife_api")
# testObj = Auth("dev_herbalife_api")
testObj.setDbSection("dev_common_db")


doLogin = {
    "nickname": "test-002",
    "email": "test-002@vhall.com",
}

testObj.doLogin(doLogin)
print(doLogin)
