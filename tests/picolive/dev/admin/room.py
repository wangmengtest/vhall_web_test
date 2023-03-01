#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.admin.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

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


