#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.huawei.v1.room import *
from utils.config_util import configUtil

testObj = Room("predev_huawei_api")
testObj.setDbSection("dev_huawei_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
vssToken = 'access:f7e4cc5e:6547a276319c02ef';
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": 'lss_cda620fe',
    'type':1,
    'from':'js',
    'num':'1',
    #'sign':'111111',
    'en':'1'
}
testObj.like(params)
