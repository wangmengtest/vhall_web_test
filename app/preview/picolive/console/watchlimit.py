#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class WatchLimit(PreviewRequest):
    def whitelogin(self, data):
        requestUtil.openDocHook("观看直播-白名单登录", self.dbUtil, ["rooms"])
        return self.post("console/watchlimit/whitelogin", data)

    def whiteleadingderive(self, data):
        requestUtil.openDocHook("控制台-观看限制-白名单模式-下载模板", self.dbUtil, ["rooms"])
        return self.post("console/watchlimit/whiteleadingderive", data)