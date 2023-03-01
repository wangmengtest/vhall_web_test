#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Produce(PreviewRequest):
    def newInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produce/switch-instance", data)

    def refreshInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance", data)

    def expireInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produce/switch-instance", data)

    def releaseInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produce/switch-instance", data)

    def upgradeInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produce/switch-instance", data)

    def tenantSync(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produce/tenantSync", data)

