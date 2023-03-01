#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Inav(PreviewRequest):
    def getAccess(self, data):
        requestUtil.openDocHook("获取网络Token", self.dbUtil, ["rooms"], False)
        return self.post("openapi/inav/access", data)

    def getRoomInfo(self, data):
        requestUtil.openDocHook("获取房间信息", self.dbUtil, ["rooms"], False)
        return self.post("openapi/inav/room-info", data)

    def getAccount(self, data):
        requestUtil.openDocHook("获取嵌入用户信息", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/inav/get-account", data)
