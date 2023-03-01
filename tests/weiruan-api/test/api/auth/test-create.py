#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("test_csces_api")
testObj.setDbSection("dev_csces_db")
# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
feAuthData = {
    "username": "zhangyu11",
    "phone": "15833684465",
    "dept":"1001A1100000009THVWW",
    "org":"0001A110000000002ZK4",
    #"dept":"",
    #"org":"0001A1100000001ARX78",#中建科工阿尔及利亚分公司
    'role_id':1,
    'from':'js'
}
testObj.testCreate(feAuthData)
