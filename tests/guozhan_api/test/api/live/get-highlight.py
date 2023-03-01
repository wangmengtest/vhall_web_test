#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.watch.live import *
from utils.config_util import configUtil

testObj = Live("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':10000,
    'show_concern':'1',
    'token' : '6b48f504c5f6e773',
    'from': 'js',
}
testObj.getHighlight(uploadParams)