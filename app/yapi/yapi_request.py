#!/usr/bin/env python
# encoding:utf8

import json
from utils.log_util import logUtil
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.db_util import DBUtil
from utils.time_util import timeUtil
from hashlib import md5

"""
YAPI 公共请求库
"""


class YapiRequest(object):
    domain = "http://chandao.ops.vhall.com:3000"
    cookie = {}

    def __init__(self):
        # 倒数最后一次的域限定
        print(self.domain)

    def setCookie(self, cookie):
        self.cookie = cookie

    def getRequestUrl(self, url):
        return "%s%s" % (self.domain, url)

    def get(self, url, data):
        print(self.cookie)
        return requestUtil.get(self.getRequestUrl(url), data, None, self.cookie)

    def post(self, url, data):
        return requestUtil.post(self.getRequestUrl(url), data, None, self.cookie)

    def postJson(self, url, data):
        return requestUtil.postJson(self.getRequestUrl(url), data, None, self.cookie)

    def upload(self, url, fileName, filePath, data):
        return requestUtil.upload(self.getRequestUrl(url), fileName, filePath, data)
