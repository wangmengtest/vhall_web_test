#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Room(VhallYunRequest):
    def checkRoomStatus(self, data):
        requestUtil.openDocHook("获取房间流状态", self.dbUtil)
        return self.post("/api/v2/room/get-stream-status", data)

    def getRoomJoinInfo(self, data):
        requestUtil.openDocHook("直播参会详情", self.dbUtil)
        return self.post("api/v1/room/get-room-join-info", data)

    def getLiveRoomUseInfo(self, data):
        requestUtil.openDocHook("直播参会详情统计", self.dbUtil)
        return self.post("/api/v2/das/get-lives-room-use-info", data)

