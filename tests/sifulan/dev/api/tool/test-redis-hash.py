#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.redis.tool import *
from utils.config_util import configUtil

testObj = Tool("dev_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
feAuthData = {
    'from':'js',
    'key':'op:interact:speaker:lss_d0c99d7b',
    'val':'{"nick_name":"test003","role_name":1,"account_id":"1009780","audio":1,"video":1}',
    'field':'1009792',
}
testObj.testRedisHash(feAuthData)
