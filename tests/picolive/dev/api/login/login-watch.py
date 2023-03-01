#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

feAuthData = {
    "nickname": "wangmeng",
    #"password": "wm123456",
    'type'    : '2',
    'from'    : 'js'
}
testObj.doIdentifyLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

