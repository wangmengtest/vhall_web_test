#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.redis.tool import *
from utils.config_util import configUtil

testObj = Tool("test_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
feAuthData = {
    'from':'js',
    'key':'op:interact:speaker:lss_f919e033',
    'val':'{"nick_name":"test002","role_name":1,"account_id":"1009793","audio":1,"video":1}',
    'field':'1009793',
}
testObj.testRedisHash(feAuthData)
