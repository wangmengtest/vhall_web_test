#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Gift(PreviewRequest):
    def addNoimage(self, data):
        requestUtil.openDocHook("礼物管理-添加礼物", self.dbUtil, ["gift"])
        return self.post("console/gift/add", data)

    def add(self, data, path):
        requestUtil.openDocHook("礼物管理-添加礼物", self.dbUtil, ["gift"])
        return self.upload("console/gift/add", 'image', path, data)

    def list(self, data):
        requestUtil.openDocHook("礼物管理-礼物列表", self.dbUtil, ["gift"])
        return self.post("console/gift/list", data)

    def send(self, data):
        requestUtil.openDocHook("礼物管理-礼物赠送", self.dbUtil, ["gift"])
        return self.post("v2/gift/send", data)
