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
    "name": "18519184446",
    "signed_at": timeUtil.getTimeIntSecond(),
    "domainName":'1',
    "flag": "1",
    "testFlag":'1',
    "authToken": "f82ece22dc3884c9d1c03175274c4d89"
}
feAuthData = {"testFlag":1,"flag":1,"orderId":"CS1906666666ABCDE","tenantCode":"example.com","timeStamp":"20220726144206961","instanceId":"3ec0a56b-fb84-4cd5-a089-3258ad5f733a","domainName":"example.tenantaccount.com","tenantId":"68cbc86abc2018ab880d92f36422fa0e","name":"huaweitenantname"}

requestData = {}
for i in sorted(feAuthData):
    requestData[i] = feAuthData[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")
for i in requestData:
    keyValueStr += "%s%s" % (i, requestData[i])
keyValueStr += configUtil.get(testObj.section, "app_secret")
print(keyValueStr)
feAuthData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
testObj.tenantSync(feAuthData)

