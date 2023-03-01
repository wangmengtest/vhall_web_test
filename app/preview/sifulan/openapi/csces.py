#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Csces(PreviewRequest):
    def allUser(self, data):
        requestUtil.openDocHook("同步中建用户", self.dbUtil, [])
        return self.post("wUser/selectUserAll", data)

    def allOrg(self, data):
        requestUtil.openDocHook("同步中建组织", self.dbUtil, [])
        return self.get("wOrgOrgs/selectIOrgAll", data)