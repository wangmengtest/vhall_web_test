#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.console.live import *
from utils.config_util import configUtil

testObj = Live("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':6689,
    'show_concern':'2',
    'from': 'js',
}
testObj.setHighlight(uploadParams)
