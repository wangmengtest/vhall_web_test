#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Document(PreviewRequest):
    def documentUpload(self, data, path):
        requestUtil.openDocHook("组件管理-上传文档 v2.0", self.dbUtil, ["document"])
        return self.upload("console/document/upload", 'document', path, data)

    def list(self, data):
        requestUtil.openDocHook("组件管理-文档列表 v2.0", self.dbUtil, ["document"])
        return self.post("console/document/list", data)

    def getInfo(self, data):
        requestUtil.openDocHook("文档管理-文档信息 v2.0", self.dbUtil, ["document"])
        return self.post("console/document/get", data)
