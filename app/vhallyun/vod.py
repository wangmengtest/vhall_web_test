#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Vod(VhallYunRequest):
    def vodToLive(self, data, status='start'):
        data['action'] = 'SubmitVODToLive'
        data['cmd'] = status

        requestUtil.openDocHook("提交点播转直播任务", self.dbUtil)
        return self.post("api/v2/vod", data)
