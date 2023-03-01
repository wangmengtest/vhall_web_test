#!/usr/bin/env python
# encoding:utf8

import require
from hashlib import md5
from app.preview.pingan.watch.vote import *
from utils.config_util import configUtil

testObj = Vote("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
testObj.setSignRequest()


data ={"app_id":"6147b94a","room_id":"lss_68c04cb1","account_id":"100384285","pagesize":20,"sign":"f931fd642142ea553c39d239d9985a0f","app_version":"210","signed_at":"1631175533","from":"ios","pingan_app_version":"1.0","token":"974d2231e253aefb","page":1,"start_type":"2","pingan_sdk_version":"2.1.0","vss_token":"access:6147b94a:30f8dd7c18a2bc34"}


requestData = {}

print("原始sign:" + data.get("sign"))
del(data['sign'])

for i in sorted(data):
    requestData[i] = data[i]

keyValueStr = configUtil.get(testObj.section, "app_secret")

for i in requestData:
    keyValueStr += "%s%s" % (i, requestData[i])

keyValueStr += configUtil.get(testObj.section, "app_secret")

print("加密前字符串:" + keyValueStr)
sign = md5(keyValueStr.encode('utf-8')).hexdigest()
print("加密得到的字符串:" + sign)
