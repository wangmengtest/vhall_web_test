#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.openapi.auth import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Auth("prod_picolive_api")
testObj.setDbSection("dev_picolive_db")

feAuthData = {
    "il_id":'60',
    "nickname": "15200000001",
    "password": "123",
    "phone": "15200000001",
    "signed_at": timeUtil.getTimeIntSecond(),
    "third_user_id":'9',
    "whitename": "15200000001",
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

