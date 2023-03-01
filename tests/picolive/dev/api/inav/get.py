#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.watch.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    "from": 'js',
    'password':'123456',
    'role_name':3,
    "il_id": 1,
}
testObj.roomGet(params)
