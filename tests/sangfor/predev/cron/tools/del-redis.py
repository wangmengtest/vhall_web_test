#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.cron.tools import *

testObj = Tools("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")

params = {
    'key':'11111111111',
    'from': 'js',
    'sign': 'vhall'
}
testObj.delRedis(params)