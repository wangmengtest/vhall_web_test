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
    'end_time':'2022-04-12 00:00:00',
    'start_time':'2022-04-12 00:00:00',
    'il_ids':'6658',
    'event':'1111',
    'page_num':'1',
    'page_size':'1000',
    'from': 'js',
}
testObj.getRecordDetailHeader(uploadParams, {'sign':'vhall022021'})
