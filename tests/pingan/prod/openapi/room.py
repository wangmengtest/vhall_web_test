#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.openapi.room import *
from utils.config_util import configUtil

testObj = Room("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
testObj.setSignRequest()

for i in range(10):
    roomStatParam = {
        "il_ids": "1100002112",
    }
    result = testObj.roomStat(roomStatParam)
# live_pv_num = result.get("data")[0]['live_pv_num']
# live_uv_num = result.get("data")[0]['live_uv_num']
# vod_pv_num = result.get("data")[0]['vod_pv_num']
# vod_uv_num = result.get("data")[0]['vod_uv_num']
#
# print(live_pv_num + vod_pv_num)
# print(live_uv_num + vod_uv_num)


realTimeStatParam = {
    "il_id": 100002434,
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

# for i in range(100):
#     incrementList = {
#         "last_max_time": "2021-09-04 20:00:00",
#         "page": i,
#         "per_page": 100,
#     }
#
#     result = testObj.incrementList(incrementList)
#
#     for data in result.get("data").get("data"):
#
#         if data.get("il_id") == 1100002324:
#             print(incrementList)
#             print(data)
#             exit()
