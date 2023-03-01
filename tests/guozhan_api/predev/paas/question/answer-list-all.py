#!/usr/bin/env python
# encoding:utf8
from app.vhallyun.question import *
from utils.config_util import configUtil
from hashlib import md5
from utils.time_util import timeUtil

testObj = Question("prod_huawei_vhallyun_api")
testObj.setDbSection("dev_huawei_db")

params = {
    'id' : '685941',
    'en':1,
    'from' : 'js',
}
#keyValueStr = configUtil.get(testObj.section, "app_secret") + "%s" % param['health_sign_time']
#param['health_sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()
testObj.getAnswerListAll(params)
