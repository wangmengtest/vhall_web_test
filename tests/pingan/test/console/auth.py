#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.auth import *
from utils.config_util import configUtil

testObj = Auth("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

feAuthData = {
    "username": "test007",
    "password": "123456",
    "log": "collect",
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

