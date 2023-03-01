#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.csces.console.export import *
from utils.config_util import configUtil

testObj = Export("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

addParam = {
    "il_id": 2,
    'begin_time': '2021-08-27',
    'end_time': '2021-08-27',
    'status': 1,
    'export': 'pv',
    'from': 'js'
}
testObj.exportLivePv(addParam)
