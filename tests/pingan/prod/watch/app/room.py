#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.watch.room import *
from utils.config_util import configUtil

testObj = Room("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()

getRoomInfoParams = {
    "il_id": 1100000750,
    "from": "js",
}
# result = testObj.roomGet(getRoomInfoParams)
#
# data = result.get("data")
# accessTokenUrl = data.get("access_token_url")
#
# print(accessTokenUrl)

# for i in range(2):
roomInfoParams = {
    "il_id": 1100001311,
}
# testObj.roomInfo(roomInfoParams)

inavGet = {
    "il_id": 1100002004,
    # "from": "android",
    # "pingan_sdk_version": "2.0.2"
}

#for i in range(2):
testObj.inavGet(inavGet)
