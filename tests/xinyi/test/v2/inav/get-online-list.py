#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.v2.inav import *
from utils.config_util import configUtil

testObj = Inav("test_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": 'lss_f17bbb3d',
    'nickname':'wangmeng5',
    'page':1,
    'page_size':20,
    'from':'js',
    'vod_id':''
}
testObj.getOnlineList(params)
