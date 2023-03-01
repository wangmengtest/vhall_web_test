#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.config_util import configUtil


class Auth(PreviewRequest):
    def doLogin(self, data, option):
        result = self.post("admin/auth/login", data)
        data = self.parseResult(result)
        token = data.get("token")

        configUtil.set(self.section, option, token)
        logUtil.renderConsole(token)
