#!/usr/bin/env python
# encoding:utf8

from app.preview.guozhan.console.live import *
from utils.config_util import configUtil

testObj = Live("dev_guozhan_api")
testObj.setDbSection("dev_guozhan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'il_id':18,
    'from': 'js',
}
testObj.getLiveInfo(uploadParams)
