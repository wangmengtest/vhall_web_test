#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.admin.room import *
from utils.config_util import configUtil

testObj = Room("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})


getStreamAddressParam = {
    "il_id": 1100000646,
}
testObj.getStreamAddress(getStreamAddressParam)

setDefaultRecordParam = {
    "record_id": "3ea67e99",
    "il_id": 1100000611
}
# testObj.setDefaultRecord(setDefaultRecordParam)


