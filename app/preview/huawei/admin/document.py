#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Document(PreviewRequest):
    def lists(self, data):
        requestUtil.openDocHook("文档管理-文档列表 v2.1", self.dbUtil, ["document"])
        return self.post("admin/document/list", data)

    def delete(self, data):
        requestUtil.openDocHook("文档管理-删除文档 v2.1", self.dbUtil, ["document"])
        return self.post("admin/document/delete", data)    

    def download(self, data):
        requestUtil.openDocHook("文档管理-下载文档 v2.1", self.dbUtil, ["document"])
        return self.post("admin/document/download", data)    