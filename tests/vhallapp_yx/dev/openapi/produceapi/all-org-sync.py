#!/usr/bin/env python
# encoding:utf8

from app.preview.vhallapp.openapi.produceapi import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Produce("dev_vhallapp_api")
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

feAuthData = {"testFlag":1,"flag":1,"orderId":"CS1906666666ABCDE","tenantCode":"example.com","timeStamp":"20220726105223104","instanceId":"515fe784e1a34419b21c975701a682a8","domainName":"example.tenantaccount.com","tenantId":"68cbc86abc2018ab880d92f36422fa0e","name":"huaweitenantname"}

requestData = {}
for i in sorted(feAuthData):
    requestData[i] = feAuthData[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")
for i in requestData:
    keyValueStr += "%s%s" % (i, requestData[i])
keyValueStr += configUtil.get(testObj.section, "app_secret")
print(keyValueStr)
feAuthData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
testObj.allOrgSync(feAuthData)

