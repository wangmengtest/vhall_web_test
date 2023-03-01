#!/usr/bin/env python
# encoding:utf8

import require
from app.yapi.yapi_request import YapiRequest
from utils.request_util import requestUtil


class User(YapiRequest):
    def login(self, data):
        requestUtil.openDocHook("登录")
        return self.post("/api/user/login_by_ldap", data)

    def getCookie(self):
        return requestUtil.cookie


userObj = User()