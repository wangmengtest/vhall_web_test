#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.watch.room import *
from utils.config_util import configUtil

testObj = Room("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
vss_token = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token': vss_token})

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

roomInfoParams = {
    "il_id": 1100000750,
}
testObj.roomInfo(roomInfoParams)
