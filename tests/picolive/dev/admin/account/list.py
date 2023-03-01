#!/usr/bin/env python
# encoding:utf8
from app.preview.picolive.admin.account import *

testObj = Account("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
params = {
    'page':1,
    'account_type':1,
    'keyword':'mengmeng',
    'begin_time':'',
    'end_time':'',
}
testObj.list(params)
