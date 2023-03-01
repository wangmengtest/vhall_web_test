#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Message(PreviewRequest):
    def clickPendant(self, data):
        requestUtil.openDocHook("消息-发送消息 v2.0", self.dbUtil, ["pendant"])
        return self.post("v2/message/send-custom-message", data)
