#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.v2.lottery import *
from utils.config_util import configUtil

testObj = Lottery("dev_picolive_api")
testObj.setDbSection("dev_pico_db")
token = configUtil.get(testObj.section, "console_token")
#testObj.setCommonData({'token': token})

param = {
    "from" : 'js',
    "vss_token" : 'access:b6f14dbf:e08c9ab317c0e90e',
    "room_id" : 'lss_8dc6baca',
    "third_party_user_id" : 2702
}
testObj.test(param)
