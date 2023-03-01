#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("test_csces_api")
testObj.setDbSection("dev_csces_db")

feAuthData = {
    "username": "wangmeng",
    "password": "123456",
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

