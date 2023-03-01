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

feAuthData = {
    "instanceId":'19d0e4986e8144469648573aa6f7777',
    "orderId": "wangmeng",
    "tenantId": "68cbc86abc2018ab880d92f36422f000",
    "tenantCode": "wm123456",
    "appId": "0bd452b0-58af-4b98-9bda-6bf59da68d57",
    "signed_at": timeUtil.getTimeIntSecond(),
    "clientId":'1',
    "clientSecret":'IlEuhNSJsZWVx2geks64BkQmk3PYYh5eJF6HYd06wAa6NJ3v33H20T5Do9aScdZHoRsHP0d8/PeKa+TssmLaf9JFChWmq3UZB7aAe2m/JpWZu6+Qv60Zt1UURh6WqNop6CUkq1Mktdey4nKPgUFuetLMpLNIu7ir0kKcKRbGJP11+e7wXIgp9PA/LbYo+9D3ExGJrTu49lVjzqOw1KbAzduHWka6RQckTYKkg8Imy4JiH9laOjdCUj5Mvfp9CGSQco9ExPqaxEyI4BHylKYxYZ/aj0379gWWhmyHTwz64LR5OBNvYLJuta956R1a8sxMiM7inkSRazhBbc5aV8aq/uuyaMkXw+GeErujFxvpvJqxO5wkyHRG3IlAMs4gfBp+3Hbw7YCYxM7lrd9quH4lDAYl+tgWyL13ZgOAaDArJfHdtlpmdcWO6V2qGPtK1bvNzsjV5qn0C+01pj6mINsJQnqWog/4zoINk5mqEfEwHiqd8sPTTwUHIY4a6/Wt9hvZdXevm6ICN5ZBaTGTIA9TGUbJSqpB8ie54xDaMzLiry6xfZgzD6vWJ/hboJVV1BNa2lzH5/z0RIyaoKRPPWvF/SMBU80xes7VMmWYHq4lN6GydIhAfzeT6zKVcmCm7ggvbVQ9QRI9yUb9MI9NzadxdAMvWuk+t2QjhJnmuSSPg80=',
    "flag": "1",
    "testFlag":'1',
    "mobilePhone":'18519184446',
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
testObj.applicationSync(feAuthData)

