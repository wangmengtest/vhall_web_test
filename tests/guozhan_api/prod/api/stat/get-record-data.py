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
    #'end_time':'2022-10-25 00:00:00',
    #'start_time':'2022-10-27 00:00:00',
    #'il_ids':'11838,12080,11886,12066,12065,12067,12085,12087,12107,11901',
    'il_ids':'12107',
    'page_size':'1000',
    'from': 'js',
    'sign':'vhall022021'
}
testObj.getRecordDataHeader(uploadParams, {'sign':'vhall022021'})
