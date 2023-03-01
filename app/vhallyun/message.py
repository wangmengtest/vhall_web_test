#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Message(VhallYunRequest):
    def lists(self, data):
        requestUtil.openDocHook("获取历史消息查询", self.dbUtil)
        return self.post("/api/v2/message/lists", data)

    def send(self, data):
        requestUtil.openDocHook("发送消息", self.dbUtil)
        return self.post("/api/v2/message/send", data)

    def sdkSend(self, data):
        requestUtil.openDocHook("发送消息", self.dbUtil)
        return requestUtil.post(self.getRequestUrl("sdk/v2/message/send"), data)



