#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Chat(PreviewRequest):
    def noticeLists(self, data):
        requestUtil.openDocHook("公告-列表", self.dbUtil, ["notices"])
        return self.post("v2/chat/notice-lists", data)