#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    "from": 'js',
    "room_id": 'lss_7f6f492e',
    "receive_account_id":1,#5飞手 4嘉宾
}
testObj.getAnchorRen(params)
