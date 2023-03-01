#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.vod import *

testObj = Vod("test_pingan_vhallyun_api")

sepPullStreamConfigParam = {
    "room_id": "lss_3d36bc84",
    "vod_id": "7be06b53",
}

testObj.vodToLive(sepPullStreamConfigParam)