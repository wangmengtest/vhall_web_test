#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Inav(PreviewRequest):
    def setAllBanned(self, data):
        requestUtil.openDocHook("全体禁言", self.dbUtil, ["rooms"], False)
        return self.post("v2/inav/set-all-banned", data)
