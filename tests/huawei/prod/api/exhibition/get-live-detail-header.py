#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.exhibition import *
from utils.config_util import configUtil

testObj = Exhibition("prod_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'end_time':'2022-12-30 00:00:00',
    'start_time':'2022-12-29 00:00:00',
    'il_ids':'12291',
    'event':'操作系统产业峰会2022w3u5',
    'from': 'js',
    'sign':'vhall022021'
}
testObj.getLiveDetailHeader(uploadParams, {'sign':'vhall022021'})
