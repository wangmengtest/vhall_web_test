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

    def getToken(self, data):
        requestUtil.openDocHook("控制台-获取临时授权 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/auth/get-token", data)

    def checkTokenExpire(self, data, option):
        requestUtil.openDocHook("检查token有效性，延长Token", self.dbUtil, ["pendant"])
        result = self.post("console/auth/check-token-expire", data)
        token = result.get("data").get("token")
        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)
        return result

    def testCreate(self, data):
        requestUtil.openDocHook("创建账号", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("api/auth/test-create", data)

    def getEnv(self, data):
        requestUtil.openDocHook("获取配置文件", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("api/auth/get-env", data)

    def autoLogin(self, data):
        requestUtil.openDocHook("中建跳转-自动登录", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("api/auth/auto-login", data)

    def loginWatch(self, data):
        requestUtil.openDocHook("中建跳转-观众登录", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("api/auth/login-watch", data)
