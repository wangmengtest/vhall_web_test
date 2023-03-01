#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

feAuthData = {
    "username": "wangmeng",
    "password": "wm123456",
    'type'    : '1',
    'from'    : 'js'
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

