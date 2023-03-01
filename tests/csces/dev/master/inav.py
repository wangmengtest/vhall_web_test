#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.inav import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Inav("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
# 设置登录信息
vss_token = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token': vss_token})



invite = {
    'room_id': '',
    'receive_account_id': '',
}
# testObj.invite(invite)
get = {
    "il_id": 1100000619,
    'from': 'js'
}
testObj.get(get)
