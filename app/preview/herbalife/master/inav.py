#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Inav(PreviewRequest):
    def inavGet(self, data):
        requestUtil.openDocHook("房间管理-房间信息", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("/v4/inav/get", data)
