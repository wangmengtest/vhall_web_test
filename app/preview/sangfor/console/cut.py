#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Cut(PreviewRequest):
    def saveRecord(self, data):
        requestUtil.openDocHook("房间管理-视频剪裁", self.dbUtil, ["rooms"])
        return self.post("console/cut/save-record", data)
