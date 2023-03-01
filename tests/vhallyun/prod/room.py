#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.room import *
from utils.time_util import timeUtil

testObj = Room("prod_wlaforum_vhallyun_api")

checkRoomStatusParam = {
    "room_ids": "lss_31194ef0,lss_1531d661,lss_5bbf2ff2,lss_bacdd3c0"
}
# testObj.checkRoomStatus(checkRoomStatusParam)


pageEach = True
roomId = "lss_bc2f49dd"

# while pageEach:
pos = 0
limit = 100
getRoomJoinInfoParam = {
    'room_id': roomId,
    'pos': pos,
    'limit': limit,
    'start_time': '2021-05-01 00:00:00',
    'end_time': '2021-06-24 23:59:59',
}
# testObj.getRoomJoinInfo(getRoomJoinInfoParam)

getLiveRoomUseInfo = {
    'room_id': 'lss_a28f2b31',
    'start_time': '2021-11-03 00:00:00',
    'end_time': '2021-11-03 17:00:01'
}
# testObj.getLiveRoomUseInfo(getLiveRoomUseInfo)