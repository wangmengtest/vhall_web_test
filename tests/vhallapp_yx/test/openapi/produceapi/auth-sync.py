#!/usr/bin/env python
# encoding:utf8

from app.preview.vhallapp.openapi.produceapi import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Produce("test_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "instanceId":'1',
    "orderId": "wangmeng",
    "tenantId": "wangmeng",
    "tenantCode": "wm123456",
    "appId": "18519184446",
    "signed_at": timeUtil.getTimeIntSecond(),
    "clientId":'1',
    "clientSecret":'111',
    "flag": "1",
    "testFlag":'1',
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
testObj.authSync(feAuthData)

