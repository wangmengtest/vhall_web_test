#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.cut import *
from utils.config_util import configUtil

testObj = Cut("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordParam = {
    'begin_time': '2021-07-01 00:00:00',
    'end_time': '2021-08-01 00:00:00',
    'il_id': '172',
    'en': '1'
}
testObj.mergeRecord(recordParam)
