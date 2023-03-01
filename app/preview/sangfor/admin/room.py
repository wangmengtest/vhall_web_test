#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Room(PreviewRequest):
    def getStreamAddress(self, data):
        requestUtil.openDocHook("获取推流地址 v2.0", self.dbUtil, ["rooms"])
        return self.post("admin/room/get-stream-address", data)

    def setDefaultRecord(self, data):
        requestUtil.openDocHook("内容-设置默认回放 v2.0", self.dbUtil, ["rooms"])
        return self.post("admin/room/set-default-record", data)

    def roomUpdateStatus(self, data):
        requestUtil.openDocHook("房间管理-修改房间状态 V2.1", self.dbUtil, ["rooms"])
        return self.post("admin/room/update-status", data)

    def pushStream(self, data):
        requestUtil.openDocHook("房间管理-创建一个拉取第三方流的配置 v2.1", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("admin/room/push-stream", data)