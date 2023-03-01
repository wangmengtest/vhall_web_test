#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil
from utils.request_util import requestUtil


class Auth(PreviewRequest):
    # 平安前端登录缓存 token
    def doLogin(self, data, option):
        result = self.post("api/auth/login-audience", data)
        token = result.get("data").get("token")
        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)

    # 有身份的人登录 助手 嘉宾
    def doIdentifyLogin(self, data, option):
        result = self.post("api/auth/login-watch", data)
        token = result.get("data").get("token")
        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)

        return result