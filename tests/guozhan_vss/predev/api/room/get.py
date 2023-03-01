#!/usr/bin/env python
# encoding:utf8
from app.preview.huaweivss.watch.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_huawei_vss")
testObj.setDbSection("dev_huawei_vss_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'room_id' : 'lss_54d904dc',
    'account_id' : '11302667',
    'sign' : 'vhall2019',
    'app_id' : configUtil.get(testObj.section, "app_id"),
    'signed_at' : timeUtil.getTimeIntSecond(),
    'from' : 'js'
}
testObj.consoleRoomGet(param)
