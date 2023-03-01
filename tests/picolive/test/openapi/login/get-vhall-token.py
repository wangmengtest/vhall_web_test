#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.openapi.auth import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Auth("test_picolive_api")
testObj.setDbSection("dev_picolive_db")

feAuthData = {
    "il_id":'326',
    "nickname": "wang",
    "password": "123",
    #"phone": "18519184446",
    "signed_at": timeUtil.getTimeIntSecond(),
    "third_user_id":'1',
    "whitename": "wang",
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
testObj.getVhallToken(feAuthData)

