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
上传服务 公共请求库
"""
class UploadRequest(object):
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

    def appendAuth(self, data):
        username = "vhall"
        password = "123456"
        date = str(timeUtil.getTimeIntSecond())
        params = [date, password]
        params = "&".join(params).encode('utf-8')
        password = md5(params).hexdigest();
        data['date'] = date
        data['Authorization'] = "%s:%s" % (username, password)

        return data
        # return self.getSignData(data)

    def get(self, url, data):
        data = self.appendAuth(data)
        return requestUtil.get(self.getRequestUrl(url), data)

    def post(self, url, data):
        data = self.appendAuth(data)
        return requestUtil.post(self.getRequestUrl(url), data)

    def upload(self, url, fileName, filePath, data):
        data = self.appendAuth(data)
        return requestUtil.upload(self.getRequestUrl(url), fileName, filePath, data)

    def parseResult(self, data):
        if 'code' not in data:
            logUtil.error("status 字段不存在")
            exit(0)

        if data['code'] != 200:
            logUtil.error(data['message'])
            exit(0)

        return data['data']
