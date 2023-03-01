#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.cut import *
from utils.config_util import configUtil

testObj = Cut("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordParam = {
    'record_id': 'd347cc87',
    'en': '1'
}
testObj.getVodInfo(recordParam)
