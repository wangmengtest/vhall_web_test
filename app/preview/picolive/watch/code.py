#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.log_util import logUtil
from utils.config_util import configUtil


class Code(PreviewRequest):
    # 笔克前端登录缓存 token
    def send(self, data):
        requestUtil.openDocHook("消息-发送消息 v2.0", self.dbUtil, ["pendant"])
        self.post("api/code/send", data)
