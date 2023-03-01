#!/usr/bin/env python
# encoding:utf8
from app.preview.picolive.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'il_id' : '1',
    'role_name':'3',
    'lang':"0",
    'from' : 'js',
}
testObj.setLang(param)
