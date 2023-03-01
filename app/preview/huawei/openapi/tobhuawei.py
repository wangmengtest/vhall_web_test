#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Tob(PreviewRequest):
    def verifyToken(self, data):
        requestUtil.openDocHook("华为tob验证token", self.dbUtil, [])
        return self.post("openapi/tob/verify-token", data)

    def highlightMyConcern(self, data, header):
        requestUtil.openDocHook("获取直播回放个性化内容", self.dbUtil, [])
        return self.getAppendHeader("api/blink/web/playback/highlightMyConcern", data, header)