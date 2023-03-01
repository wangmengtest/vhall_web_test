#!/usr/bin/env python
# encoding:utf8
from app.preview.huawei.admin.account import *

testObj = Account("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
params = {
    'page':1,
    'pagesize':10,
    'phone':'',
    'nickname':'record_share',
    #'nickname':'record_share_3513554',
    'username':'',
    'u_type':'1',
}
testObj.list(params)
