#!/usr/bin/env python
# encoding:utf8

import json
import require
import time
from urllib.parse import urlencode
from hyper.contrib import HTTP20Adapter
import random
import requests
from utils.directory_util import directoryUtil
from utils.log_util import logUtil
from utils.string_util import stringUtil
from hook.request_doc_hook import RequestDocHook

"""
公共请求类 单例
"""


class RequestUtil(object):
    requestIng = False
    proxy = None
    text = ""
    cookie = {}

    docHookDict = {
        "aspect": True,
        "open": False,
        "title": "",
        "sampleList": True,
        "dbUtil": None,
        "docList": {},
        "relationTableList": [],
    }

    # 程序上的动态切面输出文档控制
    def closeDocHookAspect(self):
        self.docHookDict["aspect"] = False

    def openDocHookAspect(self):
        self.docHookDict["aspect"] = True

    # 生成请求文档
    def openDocHook(self, title, dbUtil=None, relationTableList=None, sampleList=True):
        self.docHookDict["open"] = True
        self.docHookDict["title"] = title
        self.docHookDict["sampleList"] = sampleList

        # 生成文档需要使用的数据连接
        if dbUtil:
            self.docHookDict["dbUtil"] = dbUtil

        # 生成文档所需要的关联表
        if relationTableList:
            self.docHookDict["relationTableList"] = relationTableList

    # 关闭生成文档请求
    def closeDocHook(self):
        self.docHookDict["open"] = False
        self.docHookDict["title"] = ""
        self.docHookDict["dbUtil"] = None
        self.docHookDict["relationTableList"] = []

    # 使用代理
    def setProxy(self, proxy):
        self.proxy = proxy

    # 关闭代理
    def removeProxy(self):
        self.proxy = None

    def requestInfo(self):
        print("请求中")

    #  HTTP 请求后续操作
    def exec(self, url, requestType, data=None, jsonData=None, header=None, cookie=None, timeout=5, files=None):
        logUtil.renderConsole("执行" + requestType + "请求:" + url)

        # 随机头
        if not header:
            header = {}
        header = self.randHeaderAgent(header)
        logUtil.renderConsole("请求头 %s " % header)

        if data or jsonData:
            logUtil.renderConsole("请求体 %s" % data or jsonData)
            logUtil.renderConsole("浏览器请求 %s" % url+"?"+urlencode(data or jsonData))

        logUtil.renderConsole("请求中 ...")

        try:
            startTime = time.time()
            if requestType == 'post':
                res = requests.post(url, data, jsonData, timeout=timeout, headers=header, cookies=cookie, proxies=self.proxy)
            elif requestType == "put":
                res = requests.put(url, data, json=jsonData, timeout=timeout, headers=header, cookies=cookie, proxies=self.proxy)
            elif requestType == "delete":
                res = requests.delete(url, data=data, json=jsonData, timeout=timeout, headers=header, cookies=cookie, proxies=self.proxy)
            elif requestType == "upload":
                res = requests.post(url, data=data, json=jsonData, headers=header, cookies=cookie, files=files, proxies=self.proxy)
            else:
                res = requests.get(url, data, json=jsonData, timeout=timeout, headers=header, cookies=cookie, proxies=self.proxy)
        except Exception as e:
            print("请求失败")
            print(e)
            return False

        # 超短结构直接输出
        if len(res.text) < 10:
            print(res.status_code)
            print(res.text)

        self.cookie = requests.utils.dict_from_cookiejar(res.cookies)
        self.requestIng = False

        # 每次关闭代理
        if self.proxy:
            logUtil.renderConsole("代理: %s" % self.proxy)
            self.removeProxy()

        # 生成文档钩子
        if self.docHookDict["open"] and self.docHookDict["aspect"]:
            if jsonData:
                RequestDocHook(requestType, url, jsonData, res.text, header, cookie, self.docHookDict)
            else:
                print(res.text)
                RequestDocHook(requestType, url, data, res.text, header, cookie, self.docHookDict)

            # 钩子只执行一次，自动关闭
            self.closeDocHook()

        if res.text:
            try:
                endTime = time.time()
                result = json.loads(res.text)
                logUtil.renderConsole("总共耗时：%s" % (endTime - startTime))
                logUtil.renderConsole("请求结果为 " + stringUtil.jsonStringFormat(res.text, False))

                return result
            except Exception:
                logUtil.renderConsole("请求结果为")
                logUtil.renderConsole(res.text)

                return res.text
        else:
            logUtil.renderConsole("HTTP 状态码为 %s" % res.status_code)
            logUtil.renderConsole("请求结果为为空")
            exit()

    def get(self, url, data=None, header=None, Cookie=None, timeout=60):
        return self.exec(url, 'get', data, None, header, Cookie, timeout)

    def post(self, url, data=None, header=None, Cookie=None, timeout=60):
        return self.exec(url, 'post', data, None, header, Cookie, timeout)

    def delete(self, url, data=None, header=None, Cookie=None, timeout=60):
        return self.exec(url, 'delete', data, None, header, Cookie, timeout)

    def put(self, url, data=None, header=None, Cookie=None, timeout=60):
        return self.exec(url, 'put', data, None, data, Cookie, timeout)

    def upload(self, url, fileName, filePath, requestData=None):
        files = {fileName: open(filePath, 'rb')}
        header = None
        Cookie = None
        return self.exec(url, 'upload', requestData, None, header, Cookie, 1200, files)

    def download(self, url, path):
        directoryUtil.makeFileDir(path)
        res = requests.get(url, stream=True, headers=self.randHeaderAgent({}))

        with open(path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)

    def getJson(self, url, data=None, header=None, Cookie=None, timeout=5):
        header = self.getJsonHeader(header)
        return self.exec(url, 'get', None, data, header, Cookie, timeout)

    def postJson(self, url, data=None, header=None, Cookie=None, timeout=5):
        header = self.getJsonHeader(header)
        return self.exec(url, 'post', None, data, header, Cookie, timeout)

    def deleteJson(self, url, data=None, header=None, Cookie=None, timeout=5):
        header = self.getJsonHeader(header)
        return self.exec(url, 'delete', None, data, header, Cookie, timeout)

    def putJson(self, url, data=None, header=None, Cookie=None, timeout=5):
        header = self.getJsonHeader(header)
        return self.exec(url, 'put', None, data, header, Cookie, timeout)

    def getJsonHeader(self, header):
        if not header:
            header = {}

        header["Content-Type"] = "application/json"
        header["X-Requested-With"] = "XMLHttpRequest"

        return header


    # 随机头
    def randHeaderAgent(self, header):
        agent = [
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        header['User-Agent'] = random.sample(agent, 1)[0]
        header['Connection'] = "close"

        return header


requestUtil = RequestUtil()