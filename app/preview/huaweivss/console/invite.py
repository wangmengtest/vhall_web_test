#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.log_util import logUtil
from utils.config_util import configUtil


class Invite(PreviewRequest):

    def uploadInvite(self, data, path):
        requestUtil.openDocHook("现场-邀请上传", self.dbUtil, ["rooms", "room_supply"], False)
        #return self.post("console/liveinvite/upload", data)
        return self.upload("console/liveinvite/upload", 'file', path, data)

    def inviteList(self, data):
        requestUtil.openDocHook("现场-邀请列表", self.dbUtil, ["rooms", "room_supply"], False)
        #return self.post("console/liveinvite/upload", data)
        return self.post("console/liveinvite/invite-list", data)

    def download(self, data):
        requestUtil.openDocHook("现场-邀请下载", self.dbUtil, ["rooms", "room_supply"], False)
        #return self.post("console/liveinvite/upload", data)
        return self.post("console/liveinvite/download", data)

    def verifyCode(self, data):
        requestUtil.openDocHook("现场-邀请码验证", self.dbUtil, ["rooms", "room_supply"], False)
        #return self.post("console/liveinvite/upload", data)
        return self.post("api/liveinvite/verify-code", data)