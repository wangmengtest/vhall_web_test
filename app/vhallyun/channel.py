#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Channel(VhallYunRequest):
    def sendMessage(self, data):
        requestUtil.openDocHook("发送聊天", self.dbUtil)
        return self.post("/api/v2/message/send", data)

    def getChannelUserOnLineCount(self, data):
        requestUtil.openDocHook("获取在线连人数", self.dbUtil)
        return self.post("api/v2/das/get-channel-user-online-count", data)

    def getChannelConnectionCount(self, data):
        requestUtil.openDocHook("获取在线连接数", self.dbUtil)
        return self.post("api/v3/das/get-channel-connection-count", data)

    def checkUserOnline(self, data):
        requestUtil.openDocHook("检查用户是否在线", self.dbUtil)
        return self.post("/api/v2/channel/check-user-online", data)

    def messageLists(self, data):
        requestUtil.openDocHook("获取聊天列表", self.dbUtil, None, False)
        return self.post("/api/v2/message/lists", data)

    def getOnlineUserList(self, data):
        requestUtil.openDocHook("获取在线用户列表", self.dbUtil, None, False)
        return self.post("/api/v2/channel/get-userid-list", data)

    def getMessageState(self, data):
        requestUtil.openDocHook("获取消息状态-消息条数", self.dbUtil, None, False)
        return self.post("/api/v2/channel/send-message-stat", data)
