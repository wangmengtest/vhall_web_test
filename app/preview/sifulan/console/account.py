#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.config_util import configUtil

class Account(PreviewRequest):
    def list(self, data):
        requestUtil.openDocHook("用户管理-列表", self.dbUtil, ["account"])
        return self.post("console/account/list", data)

    def editStatus(self, data):
        requestUtil.openDocHook("用户管理-禁用/解禁", self.dbUtil, ["account"])
        return self.post("console/account/edit-status", data)

    def exportList(self, data):
        requestUtil.openDocHook("用户管理-列表-导出", self.dbUtil, ["account"])
        return self.post("console/account/export-list", data)

    def deleteTest(self, data):
        requestUtil.openDocHook("用户管理-删除测试账号", self.dbUtil, ["account"])
        return self.post("api/account/delete-test", data)
