#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'channel_id' : 'ch_55e195cc',
    'account_ids':'2',
    'from':'js'
}
testObj.onlineCheck(param)
