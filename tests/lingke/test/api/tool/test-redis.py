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
    'set':'set',
    'get':'get',
    'key':'op:interact:speaker:lss_adfc1301',
    'val':'test',
}
testObj.testRedis(feAuthData)
