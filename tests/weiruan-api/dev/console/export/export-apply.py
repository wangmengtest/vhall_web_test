#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.weiruan.console.export import *
from utils.config_util import configUtil

testObj = Export("dev_weiruan_api")
testObj.setDbSection("dev_weiruan_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
#testObj.setCommonData({'token': 'd9b0d04388fa0beb'})

addParam = {
    "il_id": 629,
    'begin_time': '2021-08-27',
    'end_time': '2021-08-27',
    'status': 1,
    'export': 'apply',
    'from': 'js'
}
testObj.exportApply(addParam)
