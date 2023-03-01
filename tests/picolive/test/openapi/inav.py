#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.openapi.inav import *
from utils.config_util import configUtil

testObj = Inav("test_pingan_api")
testObj.setDbSection("dev_picolive_db")
testObj.setSignRequest()

roomInfoParam = {
    "il_id": 1100000926,
}
testObj.getRoomInfo(roomInfoParam)
