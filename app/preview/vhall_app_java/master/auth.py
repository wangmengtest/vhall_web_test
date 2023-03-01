#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil


class Auth(PreviewRequest):
    # 平安前端登录缓存 token
    def doLogin(self, data, option):
        result = self.post("v4/account/console/auth/login", data)
        token = result.get("data").get("token")
        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)