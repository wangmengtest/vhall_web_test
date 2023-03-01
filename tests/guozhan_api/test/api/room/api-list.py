#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("test_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})

param = {
    'page' : 1,
    'status':0,
    #'keyword':'甩',
    'begin_time':'2021-08-12',
    'end_time':'2021-08-12',
    'from':'js'
}
testObj.roomApiWatchList(param)
