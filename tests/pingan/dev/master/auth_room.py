#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

# 主播获取房间信息
getRoomInfoParam = {
    'il_id': 1100001191,
    'from': 'js'
}

result = testObj.inavGet(getRoomInfoParam)
result = testObj.parseResult(result)
vss_token = result.get("vss_token")
configUtil.set(testObj.section, "vss_token", vss_token)