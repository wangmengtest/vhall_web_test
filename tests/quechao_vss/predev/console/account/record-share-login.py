#!/usr/bin/env python
# encoding:utf8
from app.preview.huawei.console.account import *

testObj = Account("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
params = {
    'il_id':'1',
    'share_token':'892574',
}
testObj.recordShareLogin(params)
