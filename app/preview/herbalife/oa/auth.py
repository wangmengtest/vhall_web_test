#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil


class Auth(PreviewRequest):
    def doLogin(self, data):
        result = self.post("v4/oa/login", data)
        logUtil.renderConsole(result)
