#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.admin.auth import *

testObj = Auth("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})

testObj.logout({})
