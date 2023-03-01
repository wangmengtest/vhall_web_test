#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.watch.chapter import *
from utils.config_util import configUtil

testObj = Chapter("prod_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':1,
    'name':'我爱你3',
    'record_id':'c017ef6e',
    'from': 'js',
}
testObj.getVodChapter(uploadParams)
