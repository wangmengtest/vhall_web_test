#!/usr/bin/env python
# encoding:utf8

from app.preview.vhallapp.openapi.produce import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Produce("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "il_id":'1',
    "nick_name": "wangmeng",
    "username": "wangmeng",
    "password": "wm123456",
    "phone": "18519184446",
    "signed_at": timeUtil.getTimeIntSecond(),
    "third_user_id":'1',
    "activity": "upgrade",
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
testObj.tenantSync(feAuthData)

