#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Health(PreviewRequest):
    def check(self, data):
        requestUtil.openDocHook("后端服务健康检测", self.dbUtil, ["ops_monitor"])
        return self.post("health/check", data)

    def mysqlCheck(self, data):
        requestUtil.openDocHook("mysql健康检测", self.dbUtil, ["ops_monitor"])
        return self.post("health/mysql-check", data)

    def redisCheck(self, data):
        requestUtil.openDocHook("redis健康检测", self.dbUtil, ["ops_monitor"])
        return self.post("health/redis-check", data)
