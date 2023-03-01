#!/usr/bin/env python
# encoding:utf8
from app.preview.csces.health.health import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Health("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

param = {
    'il_id' : '3',
    'password': '3408841',
    'role_name':'3',
    'en':1,
    'from' : 'js',
    "health_sign_time": timeUtil.getTimeIntSecond()
}
keyValueStr = configUtil.get(testObj.section, "app_secret") + "%s" % param['health_sign_time']
param['health_sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
testObj.mysqlCheck(param)
