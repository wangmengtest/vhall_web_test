#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.console.stat import *
from utils.config_util import configUtil

testObj = Stat("dev_picolive_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'page' : 1,
    'status':1,
    'il_id':'3',
    'begin_time':'2021-08-12',
    'end_time':'2021-08-26',
    'page':1
}
testObj.uvList(param)
