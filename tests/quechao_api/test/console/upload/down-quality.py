#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.console.upload import *
from utils.config_util import configUtil

testObj = Upload("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':1,
    'record_id':'6640f861',
    'quality':'1080p',
    'from': 'js',
}
testObj.downQuality(uploadParams)
