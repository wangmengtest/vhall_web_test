#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.room import *

testObj = Room("test_pingan_vhallyun_api")

checkRoomStatusParam = {
    "room_ids": "lss_31194ef0,lss_1531d661,lss_5bbf2ff2,lss_bacdd3c0"
}
testObj.checkRoomStatus(checkRoomStatusParam)
