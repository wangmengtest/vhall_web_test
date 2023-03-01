#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.master.pendant import *

testObj = Pendant("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
vss_token = testObj.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token': vss_token})

# pushScreenParams = {
#     'il_id': 1100000750,
#     'pendant_id': 20,
#     'channel_id': 'ch_6cc7b524',
#     'screen_second': 60
# }

pushScreenParams = {
    'il_id': 1100000627,
    'pendant_id': 20,
    'channel_id': 'ch_82021360',
    'screen_second': 600
}

testObj.pushScreen(pushScreenParams)

getPushListParam = {
    'account_id': 32,
    'page': 1,
    'page_size': 10,
    'keyword': '',
}
# testObj.getPushList(getPushListParam)