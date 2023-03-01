#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Produce(PreviewRequest):
    def newInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance", data)

    def refreshInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance", data)

    def expireInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switch-instance", data)

    def releaseInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switch-instance", data)

    def upgradeInstance(self, data):
        requestUtil.openDocHook("外部调用-新购商品", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switch-instance", data)

    def tenantSync(self, data):
        requestUtil.openDocHook("外部调用-租户同步", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance/produceAPI/tenantSync", data)

    def applicationSync(self, data):
        requestUtil.openDocHook("外部调用-租户同步", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance/produceAPI/applicationSync", data)

    def authSync(self, data):
        requestUtil.openDocHook("外部调用-租户同步", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance/produceAPI/authSync", data)

    def singleOrgSync(self, data):
        requestUtil.openDocHook("外部调用-租户同步", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance/produceAPI/singleOrgSync", data)

    def allOrgSync(self, data):
        requestUtil.openDocHook("外部调用-租户同步", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/produceApi/switchInstance/produceAPI/allOrgSync", data)

