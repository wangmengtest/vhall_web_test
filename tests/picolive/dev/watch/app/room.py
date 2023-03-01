#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

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

roomInfoParams = {
    "il_id": 1100000614,
}
testObj.roomInfo(roomInfoParams)
