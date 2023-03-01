#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.callback.live import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Live("dev_pingan_api")
# 设置登录信息
testObj.setSignRequest()

syncStatus = {
    "event": "lives/stream-change-status",
    "refer": "vhall",
    "time": timeUtil.getTimeIntSecond(),
    # "room_id": "lss_97f7df06",
    "room_id": "lss_69ef8277",
    "status": 2,  # 1 推流中 2 未推流
}
testObj.syncStatus(syncStatus)
