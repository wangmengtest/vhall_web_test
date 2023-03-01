#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil
from utils.request_util import requestUtil


class Admin(PreviewRequest):
    def editPassword(self, data):
        requestUtil.openDocHook("admin-密码修改", self.dbUtil, ["admin"])
        return self.post("admin/admin/edit-password", data)

    def edit(self, data):
        requestUtil.openDocHook("admin-管理员账号修改", self.dbUtil, ["admin"])
        return self.post("admin/admin/edit", data)

    def add(self, data):
        requestUtil.openDocHook("admin-管理员账号添加", self.dbUtil, ["admin"])
        return self.post("admin/admin/add", data)