#!/usr/bin/env python
# encoding:utf8
from app.preview.vhallapp.admin.account import *

testObj = Account("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
params = {
    'phone':'18519184449',
    'username':'test',
    'nick_name':'test',
    'type':1,
    'expired_at':'123'
}
testObj.add(params)
