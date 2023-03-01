#!/usr/bin/env python
# encoding:utf8
from app.preview.huawei.health.health import *
from utils.config_util import configUtil

testObj = Health("dev_huawei_vss")
testObj.setDbSection("dev_huawei_vss_db")
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
