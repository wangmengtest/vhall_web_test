#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.stat import *

testObj = Stat("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

statLiveParam = {
    "il_id": 1100000478,
    'begin_time': '2021-05-24',
    'end_time': '2021-05-24',
    'status': 1
}
# testObj.statLive(statLiveParam)

getAttendsParam = {
    # 'il_id': 1100000608,
    'il_id': 1100000610,
    'begin_time': '2021-05-1',
    'end_time': '2021-05-31',
    'data_type': 'pv',
    'attend_type': 'record',
    'merge': 0
}

testObj.getAttends(getAttendsParam)

getRealAttendsParams = {
    'il_id': 1100000478,
    'page': 1,
}
# testObj.getRealAttends(getRealAttendsParams)

exportRealAttendsParams = {
    'il_id': 1100000478,
}
# testObj.exportRealAttends(exportRealAttendsParams)


