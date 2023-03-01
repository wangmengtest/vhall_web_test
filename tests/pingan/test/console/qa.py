#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.qa import *
from utils.config_util import configUtil

testObj = Qa("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

export = {
    'il_id': '1100000619',
    'begin_time': '2021-8-9 00:00:00',
    'end_time': '2021-8-9 23:00:00',
}
testObj.export(export)