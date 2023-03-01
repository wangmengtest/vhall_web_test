#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.tob import *
from utils.config_util import configUtil
import hmac
import hashlib

testObj = Tob("prod_huawei_api")
testObj.setDbSection("dev_huawei_db")
params = {
    #'token':'afcbd16b6eee7190',
    #'token':'a63feb33f7a913fc',
    #'token':'a860fb5d239e491d',
    'token':'a63feb33f7a913fc',
}
#testObj.apiVerifyToken(params, {'sign':'vhall022021'})

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
key = 'sha256'
hsobj = hashlib.sha256(key.encode("utf-8"))
hsobj.update(keyValueStr.encode("utf-8"))
#return hsobj.hexdigest().upper()
sign = hsobj.hexdigest().upper()
sign = hashlib.sha256(keyValueStr.encode('utf-8')).hexdigest()
testObj.apiVerifyToken(params, {'sign':sign})
