#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Room(PreviewRequest):
    def inavGet(self, data):
        requestUtil.openDocHook("直播间-获取房间信息 v2.0", self.dbUtil, ["rooms"])
        return self.post("api/inav/get", data)

    def roomInfo(self, data):
        requestUtil.openDocHook("直播间-获取房间状态信息 v2.0", self.dbUtil, ["rooms"])
        return self.post("v2/room/get-info", data)

    def getInit(self, data):
        requestUtil.openDocHook("获取APP配置信息", self.dbUtil, ["rooms"], False)
        return self.post("v2/init/get-init", data)

    def getAttribute(self, data):
        requestUtil.openDocHook("观看端-获取房间属性状态", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("v2/room/get-attributes", data)

    def embed(self, data):
        requestUtil.openDocHook("嵌入地址", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("v2/room/get-info", data)

    def getAttribute(self, data):
        requestUtil.openDocHook("获取房间属性", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("/v2/room/get-attributes", data)

    def sendBullet(self, data):
        requestUtil.openDocHook("发送弹幕", self.dbUtil, ["bullet","rooms"], False)
        return self.post("/v2/room/send-bullet", data)

    def getBullet(self, data):
        requestUtil.openDocHook("获取弹幕", self.dbUtil, ["bullet","rooms"], True)
        return self.post("/v2/room/get-bullet", data)
