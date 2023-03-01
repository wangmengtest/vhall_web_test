#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.watchlimit import *
from utils.config_util import configUtil

testObj = WatchLimit("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    "en":1,
    'whitename':'wangmeng',
    'whitepaas':'123456',
    'il_id':33
}
testObj.whitelogin(params)
