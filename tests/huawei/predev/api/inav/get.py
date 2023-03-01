#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "from": 'js',
    "il_id": 1
}
testObj.consoleRoomGet(params)
