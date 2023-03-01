#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.huawei.watch.inav import *
from utils.config_util import configUtil

testObj = Inav("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
params = {
    "from": 'js',
    "il_id": 1,
    #"role_name":5,#5飞手 4嘉宾
}
testObj.getVssInfo(params)
