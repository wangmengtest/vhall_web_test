#!/usr/bin/env python
# encoding:utf8
from app.preview.picolive.admin.account import *

testObj = Account("dev_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    'page':1,
    'pagesize':10,
    'keyword':'wangmeng',
    'org':'',
    'dept':'',
}
testObj.exportList(params)
