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
    "il_id": 2,
    'begin_time': '2022-04-18',
    'end_time': '2022-04-20 19:33:34',
    'status': 1,
    'export': 'apply',
    'question_id':'11',
    'from': 'js'
}
testObj.exportList(addParam)
