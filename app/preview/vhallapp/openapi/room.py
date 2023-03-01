#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Room(PreviewRequest):
    def incrementList(self, data):
        requestUtil.openDocHook("直播间-获取统计数据", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/increment-list", data)

    def roomStat(self, data):
        requestUtil.openDocHook("直播间-获取统计数据", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/stat", data)

    def realTimeStat(self, data):
        requestUtil.openDocHook("直播间-获取实时进入房间详情 v 2.0", self.dbUtil, ["rooms"])
        return self.post("openapi/room/real-time-attends", data)

    def attends(self, data):
        requestUtil.openDocHook("获取房间观看详情", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/attends", data)

    def getAccount(self, data):
        requestUtil.openDocHook("获取房间预览", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/get-account", data)

    def getRoomIdList(self, data):
        requestUtil.openDocHook("根据房间Id获取roomId", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/get-room-id", data)

    def getRoomInfo(self, data):
        requestUtil.openDocHook("获取房间信息", self.dbUtil, ["rooms"], False)
        return self.post("openapi/room/room-info", data)