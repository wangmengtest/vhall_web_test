#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": 'lss_5edf717a',
    'from':'js'
}
testObj.endLive(params)
