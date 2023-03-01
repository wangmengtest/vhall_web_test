#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.console.room import *
from utils.config_util import configUtil

testObj = Room("test_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'il_id' : 26,
}
testObj.roomInfo(param)
