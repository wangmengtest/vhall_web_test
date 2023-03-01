#!/usr/bin/env python
# encoding:utf8
from app.preview.tcl.health.health import *
from utils.config_util import configUtil

testObj = Health("dev_tcl_api")
testObj.setDbSection("dev_tcl_db")
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
