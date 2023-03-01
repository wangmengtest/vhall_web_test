#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token':vssToken})
params = {
    "room_id": 'lss_65f9d000',
    'from':'js',
}
testObj.getAttributes(params)
