#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.watch.room import *
from utils.config_util import configUtil

testObj = Room("test_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    "from": 'js',
    "il_id": 454,
    #"role_name":2,#5飞手 4嘉宾
}
testObj.inavGet(params)
