#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.lss import *

testObj = Lss("test_pingan_vhallyun_api")


createLivePullStreamConfigParam = {
    # "room_id": "lss_e0a0825c",
    "room_id": "lss_0a515da7",
    "source_type": 0,
    "source_url": "rtmp://58.200.131.2:1935/livetv/cctv1",
    # "source_url": "rtmp://liveali.wind.com.cn/radio/roomA82027",
    "start_time": "2021-06-09 18:55:00",
    "end_time": "2021-06-09 20:00:00",
    "source_room_id": 0,
}

# testObj.createLivePullStreamConfig(createLivePullStreamConfigParam)

# testObj.describeLivePullStreamConfig()

# testObj.deleteLivePullStreamConfig({
#     "config_id": 6049
# })