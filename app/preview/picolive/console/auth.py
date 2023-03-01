#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.log_util import logUtil
from utils.config_util import configUtil


class Auth(PreviewRequest):
    def doLogin(self, data, option):
        """
        执行登录
        :param data:
        :param section:
        :return:
        """
        result = self.post("console/auth/login", data)
        result = self.parseResult(result)
        token = result.get("token")

        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)
        return result

    def getToken(self, data):
        requestUtil.openDocHook("控制台-获取临时授权 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/auth/get-token", data)

    def logout(self, data, option):
        requestUtil.openDocHook("控制台-退出", self.dbUtil, [], False)
        result = self.post("console/auth/logout", data)
        if(result['code'] == 200):
            configUtil.set(self.section, option, '')

