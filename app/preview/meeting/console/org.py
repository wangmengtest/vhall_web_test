#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.log_util import logUtil
from utils.config_util import configUtil


class Org(PreviewRequest):
    def list(self, data):
        requestUtil.openDocHook("直播平台-组织架构列表", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/org/list", data)

    def listNoneUser(self, data):
        requestUtil.openDocHook("直播平台-组织架构列表,不含用户", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/org/list-noneuser", data)

    def commonOrg(self, data):
        requestUtil.openDocHook("直播平台-同级及以下组织IDS,不含用户", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/org/common-org", data)
