#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("prod_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
#testObj.setCommonData({'token': 'e854fb17f0379dd2'})
feAuthData = {
    'from':'js'
}
testObj.getEnv(feAuthData)
