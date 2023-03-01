#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'page' : 1,
    'status':0,
    #'keyword':'甩',
    'begin_time':'2021-08-12',
    'end_time':'2021-08-12',
}
testObj.roomList(param)
