#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.huaweivss.v1.sign import *
from utils.config_util import configUtil

testObj = Sign("dev_huawei_vss")
testObj.setDbSection("dev_huawei_vss_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
vssToken = 'access:7c770daa:6c68c586da45f089'
testObj.setCommonData({'token': token, 'vss_token':vssToken})
params = {
    "room_id": '111111',
    'vss_token':'access:7c770daa:6c68c586da45f089',
    "sign_id":1,
}
testObj.signFinish(params)