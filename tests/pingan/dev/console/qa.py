#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.qa import *
from utils.config_util import configUtil

testObj = Qa("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

export = {
    'il_id': '1100001174',
    'begin_time': '2021-8-31 00:00:00',
    'end_time': '2021-8-31 23:00:00',
}
testObj.export(export)