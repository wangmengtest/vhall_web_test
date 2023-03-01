#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Document(PreviewRequest):
    def documentUpload(self, data, path):
        requestUtil.openDocHook("组件管理-上传文档 v2.0", self.dbUtil, ["document"])
        return self.upload("console/document/upload", 'document', path, data)
