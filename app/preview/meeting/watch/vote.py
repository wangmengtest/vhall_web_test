#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Vote(PreviewRequest):
    def voteAnswer(self, data):
        requestUtil.openDocHook("直播间-投票", self.dbUtil, ["rooms"])
        return self.post("v2/vote/answer", data)
