#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.cron.tools import *

testObj = Tools("prod_huawei_api")
testObj.setDbSection("dev_huawei_db")

params = {
    'key':'11111111111111111',
    'from': 'js',
    'sign': 'vhall'
}
testObj.deleteRedis(params, {'sign':'1qweds@#e2@W'})