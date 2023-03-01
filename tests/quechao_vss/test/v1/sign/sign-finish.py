#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.huaweivss.v1.sign import *
from utils.config_util import configUtil

testObj = Sign("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": 'lss_d49ddb4e',
    'end_type':1,
    'from':'js',
    'vod_id':''
}
testObj.signFinish(params)
