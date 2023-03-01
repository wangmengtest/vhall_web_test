#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.watch.pendant import *
from utils.config_util import configUtil

testObj = Pendant("prod_pingan_api")
testObj.setDbSection("dev_csces_db")

# 设置登录信息
token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': token})
testObj.setSignRequest()

clickPendantParam = {
    'il_id': 1100000924,
    'account_id': 100019273,
    'pendant_id': 50,
}
testObj.clickPendant(clickPendantParam)

getLastPendantParam = {
    'il_id': 1100000695,
}
# testObj.getLastPendant(getLastPendantParam)
