#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'room_id' : 'lss_65f9d000',
    'from':'js'
}
testObj.checkOnlineCount(param)
