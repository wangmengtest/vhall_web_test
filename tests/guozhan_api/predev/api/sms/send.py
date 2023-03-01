#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.watch.code import *
from utils.config_util import configUtil

testObj = Code("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'phone' : 18519184446,
    'from' : 'js'
}
testObj.send(param)
