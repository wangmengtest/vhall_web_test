1#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.watch.question import *
from utils.config_util import configUtil

testObj = Question("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()

watchList = {"app_id": "6147b94a", "room_id": "lss_68c04cb1", "account_id": "100384285", "pagesize": 20,
             "sign": "f931fd642142ea553c39d239d9985a0f", "app_version": "210", "signed_at": "1631175533", "from": "ios",
             "pingan_app_version": "1.0", "token": "974d2231e253aefb", "page": 1, "start_type": "2",
             "pingan_sdk_version": "2.1.0", "vss_token": "access:6147b94a:30f8dd7c18a2bc34"}

result = requestUtil.post(testObj.getRequestUrl("/v2/question/watch-list"), watchList)
print(result)
