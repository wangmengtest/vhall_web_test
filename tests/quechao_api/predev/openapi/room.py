#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.openapi.room import *
from utils.config_util import configUtil

testObj = Room("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
testObj.setSignRequest()


roomStatParam = {
    "il_ids": "1100000614,1100000613",
}
testObj.roomStat(roomStatParam)

realTimeStatParam = {
    "il_id": 1100000478,
    'start_date': '2021-01-01',
    'end_date': '2021-06-01',
    'page': 3,
    'per_page': 2,
}

# testObj.realTimeStat(realTimeStatParam)

attendsParam = {
    "il_id": 251620961,
    "type": 1,
    "start_date": "2021-01-12 00:00:00",
    "end_date": "2021-05-19 23:59:59",
    "page": 1,
    "per_page": 20,
}
# testObj.attends(attendsParam)


getAccountParam = {
}
# testObj.getAccount(getAccountParam)

getRoomIdListParam = {
    'il_ids' : '1100000478,1100000479,1100000480',
}
# testObj.getRoomIdList(getRoomIdListParam)
