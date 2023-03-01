#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.huawei.console.export import *
from utils.config_util import configUtil

testObj = Export("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
#testObj.setCommonData({'token': 'd9b0d04388fa0beb'})

addParam = {
    "task_id": 8,
    'from': 'js'
}
testObj.delete(addParam)
