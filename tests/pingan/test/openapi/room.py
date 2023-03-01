#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.pingan.openapi.room import *
from utils.config_util import configUtil

testObj = Room("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
testObj.setSignRequest()

incrementList = {
    'last_max_time': '2021-08-04 12:02:56'
}
# testObj.incrementList(incrementList)

roomStatParam = {
    "il_ids": "1100001430,1100001431,1100001432,1100001434,1100001435,1100001436,1100001437,1100001438,1100001439,1100001440,1100001442,1100001444,1100001446,1100001453,1100001454,1100001464,1100001465,1100001467,1100001468,1100001469,1100001472,1100001474,1100001478,1100001483",
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
