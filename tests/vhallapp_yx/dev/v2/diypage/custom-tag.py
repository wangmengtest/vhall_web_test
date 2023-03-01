#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.vhallapp.v2.diypage import *
from utils.config_util import configUtil

testObj = Diypage("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": 'lss_48ee9821',
    'curr_page':1,
    'page_size':20,
    'from':'js',
    'vod_id':''
}
testObj.customTag(params)
