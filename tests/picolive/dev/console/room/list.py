#!/usr/bin/env python
# encoding:utf8
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'page' : 1
}
testObj.roomList(param)
