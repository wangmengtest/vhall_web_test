#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Upload(PreviewRequest):
    def uploadList(self, data):
        requestUtil.openDocHook("内容-音视频管理列表 v2.0", self.dbUtil, ["record"])
        return self.post("console/upload/list", data)

    def delete(self, data):
        requestUtil.openDocHook("内容-删除音视频 v2.0", self.dbUtil, ["record"])
        return self.post("console/upload/del", data)