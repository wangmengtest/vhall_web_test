#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.admin.live import *
from utils.config_util import configUtil

testObj = Live("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})


params = {
    'il_id':6793,
    'limit':1,
    'status':1,
    'from': 'js',
}
testObj.channelLimit(params)
