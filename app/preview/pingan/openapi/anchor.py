#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Anchor(PreviewRequest):
    # 新增主播
    def create(self, data):
        requestUtil.openDocHook("新增主播", self.dbUtil, ["anchor"])
        return self.post("openapi/anchor/create", data)

    # 删除主播
    def delete(self, data):
        requestUtil.openDocHook("删除主播", self.dbUtil, ["anchor"])
        return self.post("openapi/anchor/delete", data)
