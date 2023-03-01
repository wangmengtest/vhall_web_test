#!/usr/bin/env python
# encoding:utf8

from hashlib import md5
from utils.time_util import timeUtil
import hmac
import hashlib
from app.preview.huawei.openapi.tob import *
from utils.config_util import configUtil

testObj = Tob("test_huawei_api")
testObj.setDbSection("dev_huawei_db")
params = {
    'token':'6b48f504c5f6e773'
}
requestData = {}
for i in sorted(params):
    requestData[i] = params[i]

keyValueStr = configUtil.get(testObj.section, "tob_secret")
str = ''
for i in requestData:
    str += i + "%s" % requestData[i];
    keyValueStr += "%s%s" % (i, requestData[i])
#str = keyValueStr
keyValueStr = keyValueStr + configUtil.get(testObj.section, "tob_secret")
print(keyValueStr)
#testObj.apiVerifyToken(params, {'sign':'vhall022021'})
sign = hashlib.sha256(keyValueStr.encode('utf-8')).hexdigest()
testObj.apiVerifyToken(params, {'sign':sign})
