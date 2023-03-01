#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.watch.room import *
from utils.config_util import configUtil
from utils.random_util import randomUtil

testObj = Room("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()

getRoomInfoParams = {
    # "il_id": 1100000620,
    # "from": "js",
    "app_version":"202",
    "from":"ios",
    "il_id":"1100000622",
    "pingan_app_version":"1.0",
    "pingan_sdk_version":"2.0.2",
    # "sign":"e44fad805b1a3984f86383cb0213914b",
    # "signed_at":"1635415400",
    "start_type":"2",
}
# result = testObj.roomInfo(getRoomInfoParams)
#
# data = result.get("data")
# accessTokenUrl = data.get("access_token_url")
#
# print(accessTokenUrl)

# roomInfoParams = {
#     "il_id": 1100000614,
# }
# testObj.roomInfo(roomInfoParams)


inavGet = {
    "il_id": 1100000620,
    "from": "android",
    "pingan_sdk_version": "2.0.2"
}
for i in range(10):
    inavGet = {
        "il_id": 1100001160 + i,
        "from": "android",
        "pingan_sdk_version": "2.0.2"
    }

    testObj.inavGet(inavGet)

# for i in range(1000):
#     for j in range(5):
#         sendBullet = {
#             "il_id": 1100000614,
#             "time": i*20,
#             "content": randomUtil.nickname('en')
#         }
#         testObj.sendBullet(sendBullet)

getBullet = {
    'il_id': '1100000614',
    'max_time': '10'
}
# result = testObj.getBullet(getBullet)

getAttribute = {
    "room_id": 'lss_8ff68147',
}
# testObj.getAttribute(getAttribute)