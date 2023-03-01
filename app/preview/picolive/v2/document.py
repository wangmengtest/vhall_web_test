#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Document(PreviewRequest):
    def documentUpload(self, data, path):
        requestUtil.openDocHook("组件管理-上传文档 v2.0", self.dbUtil, ["document"])
        return self.upload("console/document/upload", 'document', path, data)

    def download(self, data):
        requestUtil.openDocHook("资源管理-文档下载", self.dbUtil, ["document"])
        return self.post("console/document/download", data)

    def sendInvite(self, data):
        requestUtil.openDocHook("文档演示-邀请", self.dbUtil, ["document"])
        return self.post("v2/document/invite", data)

    def agreeInvite(self, data):
        requestUtil.openDocHook("文档演示-同意邀请", self.dbUtil, ["document"])
        return self.post("v2/document/agree-invite", data)

    def rejectInvite(self, data):
        requestUtil.openDocHook("文档演示-拒绝邀请", self.dbUtil, ["document"])
        return self.post("v2/document/reject-invite", data)

    def cancleInvite(self, data):
        requestUtil.openDocHook("文档演示-归还权限", self.dbUtil, ["document"])
        return self.post("v2/document/revert-invite", data)
