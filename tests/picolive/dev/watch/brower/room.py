#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")


# 设置登录信息
# vss_token = configUtil.get(testObj.section, "vss_token")
# testObj.setCommonData({'vss_token': vss_token})
#

getRoomInfoParams = {
    "il_id": 131,
    "from": "js",
    # "token": "9d54c979ea8d4508",
}
result = testObj.roomGet(getRoomInfoParams)
#
# data = result.get("data")
# accessTokenUrl = data.get("access_token_url")
#
# print(accessTokenUrl)

# roomInfoParams = {
#     "il_id": 1100000750,
# }
# testObj.roomInfo(roomInfoParams)
