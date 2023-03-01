#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.exhibition import *
from utils.config_util import configUtil

testObj = Exhibition("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':'6658',
    'page':'1',
    'page_size':'1000',
    'from': 'js',
    'sign':'vhall022021'
}
testObj.getQaListHeader(uploadParams, {'sign':'vhall022021'})
