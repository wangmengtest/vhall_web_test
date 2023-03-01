#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.callback import *
from utils.time_util import timeUtil

# testObj = Callback("prod_pingan_api")
# testObj = Callback("prod_azure_api")
testObj = Callback("test_xiaomi_api")

streamChangeStatus = {
    'room_id': 'lss_74b91e0c',
    'status': 2,
    'time': timeUtil.getTimeIntSecond()
}
testObj.streamChangeStatus(streamChangeStatus)
#
# liveIndex = {
#
# }
#
# result = testObj.liveIndex(liveIndex)
# print(result)