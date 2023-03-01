#!/usr/bin/env python
# encoding:utf8
from app.preview.vhallapp.admin.account import *

testObj = Account("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
params = {
    'page':1,
    'pagesize':10,
    #'keyword':'wangmeng',
    'type':'2'
}
testObj.list(params)
