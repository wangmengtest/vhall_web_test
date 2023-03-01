#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.console.room import *
from utils.config_util import configUtil

testObj = Room("prod_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
testObj.setCommonData({'token': '619fb42413bd44dd'})

param = {
    'room_id' : 'lss_b1c7c96c',
}
testObj.roomInfo(param)
