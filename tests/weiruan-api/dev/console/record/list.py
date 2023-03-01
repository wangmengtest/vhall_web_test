#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.console.record import *
from utils.config_util import configUtil

testObj = Record("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
token = "c9f8b51f778f53e9"
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':1,
    'from': 'js',
}
testObj.list(uploadParams)
