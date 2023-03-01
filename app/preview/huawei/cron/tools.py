#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Tools(PreviewRequest):
    def getEnv(self, data, header):
        requestUtil.openDocHook("获取env", self.dbUtil, ["record"])
        return self.postAppendHeader("cron/tools/get-env", data, header)

    def deleteRedis(self, data, header):
        requestUtil.openDocHook("删除redis", self.dbUtil, ["record"])
        return self.postAppendHeader("cron/tools/delete-redis", data, header)

    def delRedis(self, data):
        requestUtil.openDocHook("删除redis", self.dbUtil, ["record"])
        return self.post("cron/tools/del-redis", data)