#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.watch.inav import *
from utils.config_util import configUtil

testObj = Inav("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "from": 'js',
    "room_id": 'lss_65f9d000',
    'type':1
}
testObj.setAllBanned(params)
