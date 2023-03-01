#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.log_util import logUtil


class Room(PreviewRequest):
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
        return self.post("v2/room/get", data)

    def getInit(self, data):
        requestUtil.openDocHook("获取APP配置信息", self.dbUtil, ["rooms"], False)
        return self.post("v2/init/get-init", data)

    def getAttribute(self, data):
        requestUtil.openDocHook("观看端-获取房间属性状态", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("v2/room/get-attributes", data)

    def checkRoomPassword(self, data):
        requestUtil.openDocHook("检查房间口令", self.dbUtil, ["rooms", "room_invited"])
        return self.post("api/room/check-room-password", data)

    def setLang(self, data):
        requestUtil.openDocHook("设置观看直播的页面语言", self.dbUtil, ["rooms", "room_invited"])
        return self.post("api/room/set-lang", data)
