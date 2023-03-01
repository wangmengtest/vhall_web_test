#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil
from utils.request_util import requestUtil


class Callback(PreviewRequest):
    def callbackIndex(self, data):
        requestUtil.openDocHook("中建回调-中建回调", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("callback/lives/index", data)

    def recordCallbackIndex(self, data):
        requestUtil.openDocHook("中建回调-中建回调", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("callback/lives/index", data)