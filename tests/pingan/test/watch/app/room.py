#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.watch.room import *
from utils.config_util import configUtil

testObj = Room("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()

getRoomInfoParams = {
    "il_id": 1100001239,
    "from": "js",
}
# result = testObj.inavGet(getRoomInfoParams)
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


getAttribute = {
    "room_id": 'lss_9d7198fa',
}
testObj.getAttribute(getAttribute)
