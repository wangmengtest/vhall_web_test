#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil
from utils.request_util import requestUtil


class Account(PreviewRequest):
    def add(self, data):
        requestUtil.openDocHook("admin-添加主持人账号", self.dbUtil, ["accounts"])
        return self.post("admin/account/add", data)

    def edit(self, data):
        requestUtil.openDocHook("admin-编辑主持人账号", self.dbUtil, ["accounts"])
        return self.post("admin/account/edit", data)

    def list(self, data):
        requestUtil.openDocHook("admin-主持人账号列表", self.dbUtil, ["accounts"])
        return self.post("admin/account/list", data)
