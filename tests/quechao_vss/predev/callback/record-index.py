#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.huaweivss.callback.callback import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Callback("dev_huawei_vss")
testObj.setDbSection("dev_huawei_vss_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
#testObj.setCommonData({'token': token})

feAuthData = {
    #"username": "wangmeng",
    "signed_att": timeUtil.getTimeIntSecond(),
    "event":'SingleTranscodeComplete'
}
requestData = {}
for i in sorted(feAuthData):
    requestData[i] = feAuthData[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")
keyValueStr = (md5(keyValueStr.encode('utf-8')).hexdigest())
str = ''
for i in requestData:
    print(i)
    print(requestData[i])
    str += i + "|" + keyValueStr + "|" + "%s" % requestData[i];
    #keyValueStr += "%s%s" % (i, requestData[i])
print(str)
print(md5(str.encode('utf-8')).hexdigest())
#keyValueStr += configUtil.get(testObj.section, "app_secret")
#print(keyValueStr)
#feAuthData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
feAuthData['signature'] = md5(str.encode('utf-8')).hexdigest()
testObj.recordCallbackIndex(feAuthData)
