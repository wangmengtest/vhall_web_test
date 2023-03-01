#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.health.health import *
from utils.config_util import configUtil

testObj = Health("test_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'il_id' : '3',
    'password': '3408841',
    'role_name':'3',
    'en':1,
    'from' : 'js',
}
testObj.check(param)
