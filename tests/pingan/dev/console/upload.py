#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.upload import *
from utils.config_util import configUtil

testObj = Upload("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordListParam = {
    "page": 1,
    "pagesize": 100,
}
# testObj.uploadList(recordListParam)

delete = {
    'record_id': '88fbad9c',
}
testObj.delete(delete)
