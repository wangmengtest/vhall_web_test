#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

params = {
    "il_id": 3,
    'from': 'js'
}
testObj.editStatus(params)
