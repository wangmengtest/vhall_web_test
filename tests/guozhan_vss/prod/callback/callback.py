#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.callback.callback import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Callback("prod_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
#testObj.setCommonData({'token': token})

feAuthData = {
    #"username": "wangmeng",
    "signed_att": timeUtil.getTimeIntSecond()
}
requestData = {}
for i in sorted(feAuthData):
    requestData[i] = feAuthData[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")
print(md5(keyValueStr.encode('utf-8')).hexdigest())
str = ''
for i in requestData:
    print(i)
    print(requestData[i])
    str += i + "|" + md5(keyValueStr.encode('utf-8')).hexdigest() + "|" + "%s" % requestData[i];
    keyValueStr += "%s%s" % (i, requestData[i])
print(str)
#keyValueStr += configUtil.get(testObj.section, "app_secret")
#print(keyValueStr)
#feAuthData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
feAuthData['signature'] = md5(str.encode('utf-8')).hexdigest()
testObj.callbackIndex(feAuthData)
