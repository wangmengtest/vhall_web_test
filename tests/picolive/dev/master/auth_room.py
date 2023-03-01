#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

# 主播获取房间信息
getRoomInfoParam = {
    'il_id': 1100000696,
    'from': 'js'
}

result = testObj.roomInfo(getRoomInfoParam)
result = testObj.parseResult(result)
vss_token = result.get("vss_token")
configUtil.set(testObj.section, "vss_token", vss_token)