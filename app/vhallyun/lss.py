#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Lss(VhallYunRequest):
    def createLivePullStreamConfig(self, data):
        requestUtil.openDocHook("创建拉流配置", self.dbUtil)
        return self.post("api/v2/room/create-live-pull-stream-config", data)

    def describeLivePullStreamConfig(self):
        requestUtil.openDocHook("获取拉流配置", self.dbUtil, None, False)
        return self.post("api/v2/room/describe-live-pull-stream-config", {})

    def deleteLivePullStreamConfig(self, data):
        requestUtil.openDocHook("删除拉流配置", self.dbUtil, None, False)
        return self.post("api/v2/room/delete-live-pull-stream-config", data)
