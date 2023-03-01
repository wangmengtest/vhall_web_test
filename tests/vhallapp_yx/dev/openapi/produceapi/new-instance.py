#!/usr/bin/env python
# encoding:utf8

from app.preview.vhallapp.openapi.produceapi import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Produce("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "mobilePhone": "18519184466",
    "businessId": timeUtil.getTimeIntSecond(),
    "expireTime":'201706211855321',
    "activity": "newInstance",
    "timeStamp":"201706211855321",
    "authToken": "f82ece22dc3884c9d1c03175274c4d89"
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
testObj.newInstance(feAuthData)

