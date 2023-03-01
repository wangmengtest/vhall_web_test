#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.console.chapter import *
from utils.config_util import configUtil

testObj = Chapter("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':1,
    'name':'我爱你3',
    'document_id':'48a50999,e2de8493',
    'from': 'js',
}
testObj.get(uploadParams)
