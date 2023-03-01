#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.vhallapp.market.auth import *
from utils.config_util import configUtil

testObj = Auth("test_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "from":'web',
    "market_code": "liuweifei",
    "market_tenant": "ceshi"
}
testObj.marketLogin(feAuthData)

# token = configUtil.get(testObj.section, "console_token")

# testObj.setCommonData({'token': token})

# checkTokenExpire = {
#     'token': 'effc95c374abfec7'
# }
# testObj.checkTokenExpire(checkTokenExpire, 'console_token')
