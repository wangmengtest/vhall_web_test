#!/usr/bin/env python
# encoding:utf8

import json
from utils.log_util import logUtil
from hashlib import md5
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.time_util import timeUtil

"""
Vhall 公共请求库
"""


class PinganRequest(object):
    domain = None
    section = None
    header = {}
    cookie = {}
    token = None
    vss_token = None

    def __init__(self, parentSection="local", parentOption="api"):
        section = configUtil.get(parentSection, parentOption)

        # 倒数最后一次的域限定
        self.section = section
        self.setConfigByCurrentSection()

    # 通过域桶盖修改配置
    def setConfigByCurrentSection(self):
        self.domain = configUtil.get(self.section, "domain")

    # 设置请求头
    def setHeader(self, key, value):
        self.header[key] = value

    def getRequestUrl(self, url):
        return "%s/%s" % (self.domain, url)

    def get(self, url, data):
        if not data:
            data = {}
        data = self.getSignData(data)

        return requestUtil.get(self.getRequestUrl(url), data, self.header)

    def post(self, url, data):
        if not data:
            data = {}
        data = self.getSignData(data)

        return requestUtil.post(self.getRequestUrl(url), data, self.header)

    # 设置请求Token 一次销毁
    def setAppToken(self):
        self.token = configUtil.get(self.section, "app_token")

    def getSignData(self, data):
        sortData = {}

        # 填充Token 一次销毁
        if self.token:
            data['token'] = self.token
            self.token = None

        data['app_id'] = configUtil.get(self.section, "app_id")
        data['signed_at'] = timeUtil.getTimeIntSecond()

        for i in sorted(data):
            sortData[i] = data[i]

        keyValueStr = configUtil.get(self.section, "app_secret")
        for i in sortData:
            keyValueStr += "%s%s" % (i, sortData[i])

        keyValueStr += configUtil.get(self.section, "app_secret")
        print(keyValueStr)
        sortData['sign'] = md5(keyValueStr.encode('utf-8')).hexdigest()

        return sortData
