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
    'subject': '测试',
    'begin_time': '2021-10-18 11:18:00',
    'end_time': '2021-10-18 11:18:30',
}
testObj.roomWatchList(param)
