#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.watch.pendant import *
from utils.config_util import configUtil

testObj = Pendant("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': token})
testObj.setSignRequest()

clickPendantParam = {
    'il_id': 1100000627,
    'account_id': 100019273,
    'pendant_id': 20,
}
# testObj.clickPendant(clickPendantParam)

getLastPendantParam = {
    'il_id': 1100000695,
}
testObj.getLastPendant(getLastPendantParam)
