#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Live(PreviewRequest):
    def setHighlight(self, data):
        requestUtil.openDocHook("房间编辑-设置个性化回放配置", self.dbUtil, ["rooms"])
        return self.post("console/live/set-highlight", data)

    def getHighlight(self, data):
        requestUtil.openDocHook("观看端-获取个性化回放配置-透穿到华为接口", self.dbUtil, ["rooms"])
        return self.post("api/live/owner-concern", data)

    def getLiveInfo(self, data):
        requestUtil.openDocHook("房间编辑-获取live信息", self.dbUtil, ["rooms"])
        return self.post("console/live/get", data)

    def getAccessToken(self, data):
        requestUtil.openDocHook("房间编辑-获取live信息", self.dbUtil, ["rooms"])
        return self.post("console/live/get-access-token", data)

    def channelLimit(self, data):
        requestUtil.openDocHook("admin房间列表-聊天限频", self.dbUtil, ["rooms"])
        return self.post("admin/live/channel-limit", data)

    def getChannelLimit(self, data):
        requestUtil.openDocHook("admin房间列表-聊天限频", self.dbUtil, ["rooms"])
        return self.post("admin/live/get-channel-limit", data)
