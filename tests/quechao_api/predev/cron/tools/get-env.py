#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.cron.tools import *

testObj = Tools("predev_huawei_api")
testObj.setDbSection("dev_huawei_db")

params = {
    'il_id':1,
    'name':'我爱你3',
    'document_id':'03c8c95b',
    'from': 'js',
    'sign': 'vhall'
}
testObj.getEnv(params, {'sign':'1qweds@#e2@W'})