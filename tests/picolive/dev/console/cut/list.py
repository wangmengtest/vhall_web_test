#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.cut import *
from utils.config_util import configUtil

testObj = Cut("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordParam = {
    'keywords': '172',
    'en': '1'
}
testObj.list(recordParam)
