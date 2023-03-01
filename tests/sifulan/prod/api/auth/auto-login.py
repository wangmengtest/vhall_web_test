#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Auth("prod_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
#testObj.setCommonData({'token': token})

feAuthData = {
    "username": "liuweifei",
    "signed_at": timeUtil.getTimeIntSecond()
}
requestData = {}
for i in sorted(feAuthData):
    requestData[i] = feAuthData[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")
for i in requestData:
    keyValueStr += "%s%s" % (i, requestData[i])

keyValueStr += configUtil.get(testObj.section, "app_secret")
print(keyValueStr)
feAuthData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
#feAuthData['sign'] = "test"
testObj.autoLogin(feAuthData)
