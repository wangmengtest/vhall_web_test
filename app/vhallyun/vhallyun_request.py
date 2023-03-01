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
微吼云 公共请求库
"""
class VhallYunRequest(object):
    domain = None
    section = None
    dbUtil = None

    def __init__(self, section):
        # 倒数最后一次的域限定
        self.section = section
        self.setConfigByCurrentSection()

    def setDbSection(self, env=False):
        if env:
            self.dbUtil = DBUtil(env)

    # 通过域桶盖修改配置
    def setConfigByCurrentSection(self):
        self.domain = configUtil.get(self.section, "domain")

    def getRequestUrl(self, url):
        return "%s/%s" % (self.domain, url)

    def appendAuth(self, data, signStr="sign"):
        return self.getSignData(data, signStr)

    def get(self, url, data, signStr="sign"):
        data = self.appendAuth(data, signStr)
        return requestUtil.get(self.getRequestUrl(url), data)

    def post(self, url, data, signStr="sign"):
        data = self.appendAuth(data, signStr)
        return requestUtil.post(self.getRequestUrl(url), data)

    def postJson(self, url, data, signStr="sign"):
        data = self.appendAuth(data, signStr)
        return requestUtil.postJson(self.getRequestUrl(url), data)

    def upload(self, url, fileName, filePath, data):
        data = self.appendAuth(data)
        return requestUtil.upload(self.getRequestUrl(url), fileName, filePath, data)

    def getSignData(self, data, signStr="sign"):
        """
        接口请求校验
        :param data:
        :param signStr
        :return:
        """
        requestData = {}

        data['app_id'] = configUtil.get(self.section, "app_id")
        data['signed_at'] = timeUtil.getTimeIntSecond()

        for i in sorted(data):
            requestData[i] = str(data[i])

        keyValueStr = configUtil.get(self.section, "app_secret")
        for i in requestData:
            keyValueStr += "%s%s" % (i, requestData[i])

        keyValueStr += configUtil.get(self.section, "app_secret")
        requestData[signStr] = md5(keyValueStr.encode('utf-8')).hexdigest()

        return requestData

    def parseResult(self, data):
        if 'code' not in data:
            logUtil.error("status 字段不存在")
            exit(0)

        if data['code'] != 200:
            logUtil.error(data['message'])
            exit(0)

        return data['data']
