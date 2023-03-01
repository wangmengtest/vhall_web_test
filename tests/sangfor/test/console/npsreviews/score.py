#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.watch.live import *
from utils.config_util import configUtil

testObj = Live("test_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':6731,
    'score':'1',
    'token' : '3fb405c202db3841',
    'from': 'js',
}
testObj.npsReviewsScore(uploadParams)
