#!/usr/bin/env python
# encoding:utf8
from app.preview.vhallapp.admin.account import *

testObj = Account("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
params = {
    'phone':'18519184446',
    'username':'test',
    'nick_name':'test',
    'expired_at':'123',
    'account_id':1000001,
}
testObj.edit(params)
