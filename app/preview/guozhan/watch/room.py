#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.log_util import logUtil


class Room(PreviewRequest):
    def roomGet(self, data):
        requestUtil.openDocHook("直播间-获取房间状态信息 v2.0", self.dbUtil, ["rooms"])
        return self.post("v2/room/get-info", data)

    def inavGet(self, data, option = 'vss_token'):
        requestUtil.openDocHook("直播间-获取房间信息 v2.0", self.dbUtil, ["rooms"])
        result = self.post("api/inav/get", data)
        result = self.parseResult(result)
        vssToken = result.get("vss_token")
        configUtil.set(self.section, option, vssToken)
        logUtil.renderConsole(vssToken)
        return result

    def roomGet(self, data, option = 'vss_token'):
        requestUtil.openDocHook("直播间-获取房间信息", self.dbUtil, ["rooms", "room_supply"])
        result = self.post("api/v1/inav/get", data)
        result = self.parseResult(result)
        vssToken = result.get("vss_token")
        configUtil.set(self.section, option, vssToken)
        logUtil.renderConsole(vssToken)
        return result

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

    def roomList(self, data):
        requestUtil.openDocHook("观看端-房间列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/list", data)

    def roomApiWatchList(self, data):
        requestUtil.openDocHook("观看端-房间列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/watch-list", data)

    def checkOnlineCount(self, data):
        requestUtil.openDocHook("观看端-观看房间检查观看人数", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/check-online-count", data)

    def onlineCheck(self, data):
        requestUtil.openDocHook("观看端-检查用户状态", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/online-check", data)

    def getAttributes(self, data):
        requestUtil.openDocHook("直播端-获取房间属性", self.dbUtil, ["rooms", "room_join"])
        return self.post("v2/room/get-attributes", data)

    def consoleRoomGet(self, data):
        requestUtil.openDocHook("观看端-房间信息", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/get", data)

    def createAudienceInvited(self, data):
        requestUtil.openDocHook("观看端-保存观众信息", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/room/update-invited-audience", data)

    def getAnchorRen(self, data):
        requestUtil.openDocHook("观看端-获取主持人信息", self.dbUtil, ["rooms", "room_join"])
        return self.post("api/v1/inav/get-anchor-ren", data)

    def getRoomInvited(self, data):
        requestUtil.openDocHook("控制台-获取房间邀请信息", self.dbUtil, ["rooms"], False)
        return self.post("api/v1/room/get-room-invited", data)

