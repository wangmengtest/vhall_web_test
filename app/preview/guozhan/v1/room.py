#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Room(PreviewRequest):
    def like(self, data):
        requestUtil.openDocHook("观众端-点赞", self.dbUtil, ["likes"])
        return self.post("vss/room/like", data)