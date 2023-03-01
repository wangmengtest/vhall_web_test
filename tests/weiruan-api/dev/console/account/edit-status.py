#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.console.account import *

testObj = Account("dev_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    'user_id':2,
    'status':0
}
testObj.editStatus(params)
