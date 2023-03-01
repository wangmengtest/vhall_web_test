#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.stat import *

testObj = Stat("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

statLiveParam = {
    "il_id": 1100002112,
    'begin_time': '2021-09-01',
    'end_time': '2021-09-01',
    'status': 1
}
testObj.statLive(statLiveParam)

getAttendsParam = {
    # 'il_id': 1100000608,
    'il_id': 1100000610,
    'begin_time': '2021-05-1',
    'end_time': '2021-05-31',
    'data_type': 'pv',
    'attend_type': 'record',
    'merge': 0
}

# testObj.getAttends(getAttendsParam)

getRealAttendsParams = {
    'il_id': 1100000478,
    'page': 1,
}
# testObj.getRealAttends(getRealAttendsParams)

exportRealAttendsParams = {
    'il_id': 1100000478,
}
# testObj.exportRealAttends(exportRealAttendsParams)


