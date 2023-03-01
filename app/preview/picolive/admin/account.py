#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.config_util import configUtil

class Account(PreviewRequest):
    def list(self, data):
        requestUtil.openDocHook("用户管理-列表", self.dbUtil, ["account"])
        return self.post("admin/account/list", data)

    def add(self, data):
        requestUtil.openDocHook("用户管理-创建主持人账号", self.dbUtil, ["account"])
        return self.post("admin/account/add", data)

    def exportList(self, data):
        requestUtil.openDocHook("用户管理-列表-导出", self.dbUtil, ["account"])
        return self.post("admin/account/export-list", data)
