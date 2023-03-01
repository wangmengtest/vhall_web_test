#!/usr/bin/env python
# encoding:utf8
import require
import json
import os

from utils.config_util import configUtil
from utils.log_util import logUtil
from utils.html_render_util import htmlRenderUtil
from utils.string_util import stringUtil

"""
生成请求文档钩子
"""


class RequestDocHook(object):
    def __init__(self, requestType=None, requestUrl=None, requestData=None,
                 response=None, header=None, cookie=None, docHookDict=None):
        self.requestType = str(requestType)
        self.requestUrl = str(requestUrl)
        self.requestData = requestData
        self.header = header
        self.cookie = cookie
        self.docHookDict = docHookDict

        try:
            if isinstance(response, str) and response:
                jsonResponse = json.loads(response)

                # 是否简化输出列表
                if self.docHookDict["sampleList"]:
                    self.responseData = self.sampleList(jsonResponse)
                else:
                    self.responseData = jsonResponse
            else:
                self.responseData = response
        except Exception:
            # 长度超过 100 通过浏览器渲染查看
            if len(response) > 100:
                htmlRenderUtil.render(response, False)
                filePath = require.logPath("/html.html")
                self.openInChrome(filePath)

            exit()

        self.composeRequestHead()
        self.composeRequestType()
        self.composeRequestUrl()
        self.composeRequestData()
        self.composeResponseData()
        self.composeRequestExample()
        self.composeResponseExample()

        # 通过浏览器查看文档
        # filePath = require.logPath("/log.log")
        # self.openInChrome(filePath)

    def openInChrome(self, filePath):
        logUtil.renderConsole("正在打开浏览器")
        command = "%s file://%s" % (configUtil.get("env", "chrome"), filePath)
        os.system(command)

    # 文件jsonSchema基础形态
    def getJsonSchemaTemplate(self, data=None):
        if data is None:
            data = []

        return {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": data,
            "required": [],
        }

    def composeRequestHead(self):
        if self.docHookDict["title"]:
            logUtil.render("接口名称:   %s" % self.docHookDict["title"], False)

    def composeRequestType(self):
        logUtil.render("接口类型:   %s" % self.requestType.upper(), False)

    def composeRequestUrl(self):
        # 倒数第二个斜线划分最终地址
        logUtil.render("接口地址为:  %s" % self.requestUrl, False)
        requestUrlSplit = self.requestUrl.split("com")
        if len(requestUrlSplit) >= 2:
            requestUrlSplit = requestUrlSplit[-1:][0]
            requestUrlSplit = requestUrlSplit.split("/")
        else:
            requestUrlSplit = self.requestUrl.split("/")
            requestUrlSplit = requestUrlSplit[-2:]

        for key, value in enumerate(requestUrlSplit):
            if stringUtil.isNumber(value):
                requestUrlSplit[key] = "{id}"


        logUtil.render("文档地址:   %s" % "/".join(requestUrlSplit), False)

    def composeRequestData(self):
        if self.requestType == "get":
            logUtil.render("请求参数", False)
            if self.requestData:
                for i in self.requestData:
                    comment = self.composeValueDescription(i, "")
                    logUtil.render("%s:%s    %s" % (i, self.requestData[i], comment), False, 1)
        else:
            data = self.composeData(False, self.requestData)
            template = self.getJsonSchemaTemplate(data)
            logUtil.render("请求参数JsonSchema", False)
            logUtil.renderJson(template, False)

    def composeResponseData(self):
        data = self.composeData(False, self.responseData, True)
        template = self.getJsonSchemaTemplate(data)
        logUtil.render("\r", False, 0)
        logUtil.render("\r返回参数JsonSchema", False)
        logUtil.renderJson(template, False)

    def composeRequestExample(self):
        if self.requestData:
            logUtil.render("请求参数示例", False)
            logUtil.render("```", False)
            logUtil.renderJson(self.requestData)
            logUtil.render("```", False)

    def composeResponseExample(self):
        logUtil.render("响应参数示例", False)
        logUtil.render("```", False)
        logUtil.renderJson(self.responseData)
        logUtil.render("```", False)

    def sampleList(self, data):
        if isinstance(data, list):
            data = data[0: 2]
            for key, value in enumerate(data):
                if isinstance(value, list) or isinstance(value, dict):
                    data[key] = self.sampleList(value)
                else:
                    data[key] = value
            return data
        elif isinstance(data, dict):
            result = {}
            for i in data:
                if isinstance(data[i], list) or isinstance(data[i], dict):
                    result[i] = self.sampleList(data[i])
                else:
                    result[i] = data[i]
            return result
        else:
            return data

    def composeData(self, key, data, excludeFirstData=False):
        result = {}
        if not data:
            return result

        if isinstance(data, list):
            result = self.composeData(key, data[0])

        elif isinstance(data, dict):
            for dictKey in data:
                value = data[dictKey]
                if isinstance(value, dict):
                    finalData = self.composeData(dictKey, value)

                    result[dictKey] = {
                        "type": "object",
                        "properties": finalData
                    }
                elif isinstance(value, list):
                    finalData = self.composeData(dictKey, value)
                    result[dictKey] = {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": finalData
                        }
                    }

                else:
                    if stringUtil.isNumber(value):
                        valueType = "number"
                    else:
                        valueType = "string"

                    description = ""
                    if not excludeFirstData or (excludeFirstData and key):
                        # 业务注释
                        description = self.composeValueDescription(dictKey, value)
                    else:
                        # 外层结构
                        if dictKey == "status":
                            description = "HTTP 状态 200 成功 !200 失败"
                        if dictKey == "message":
                            description = "请求错误信息描述"
                        if dictKey == "request_id":
                            description = "请求编号，有错误时发给后端"

                    result[dictKey] = {
                        "type": valueType,
                        "mock": "",
                        "description": description
                    }

        return result

    def composeValueDescription(self, columnKey, default):
        # 有关联表，通过关联表查询字段含义
        if self.docHookDict['dbUtil'] and self.docHookDict['relationTableList']:
            if not self.docHookDict['docList']:
                self.docHookDict['docList'] = self.getPreDefinedCommentDict()

                dbUtil = self.docHookDict['dbUtil']
                tables = []

                for _, tableName in enumerate((self.docHookDict['relationTableList'])):
                    sql = "SHOW TABLE STATUS WHERE NAME LIKE"
                    sqlBandList = ["%" + tableName + "%"]
                    sql += " %s "
                    lisTable = dbUtil.select(sql, sqlBandList)
                    
                    for eachTable in lisTable:
                        tables.append(eachTable)

                for table in tables:
                    tableColumns = dbUtil.select("SHOW FULL COLUMNS FROM %s" % table.get("Name"))
                    for column in tableColumns:
                        field = column.get("Field")
                        comment = column.get("Comment")

                        if field not in self.docHookDict['docList'] and comment:
                            self.docHookDict['docList'][field] = comment

        if columnKey in self.docHookDict['docList']:
            return self.docHookDict['docList'][columnKey].replace("\r\n", " ")

        else:
            return default

        

    # 获取预定义的字典明细
    def getPreDefinedCommentDict(self):
        return {
            "page": "页码",
            "pagesize": "每页条目",
            "id": " ID",
            "total": "总条目",
            "total_page": "总页码",
            "laravel_through_key":  "关联表ID,无需关注",
            "list": "数据列表",
            "token": "用户授权码",
            "first_page_url": "首页地址",
            "from": "来源页码",
            "last_page": "最后一页页码",
            "last_page_url": "最后一页地址",
            "next_page_url": "下一页地址",
            "path": "根路径",
            "per_page": "每页条目",
            "prev_page_url": "",
            "to": "",
            "pf": "观看终端 ，0代表iOSAPP，1代表AndroidAPP，2代表flash，3代表wap，4代表IOSSDK，5代表AndroidSDK，6代表小助手，7代表JS播放器WEB端，9代表微信小程序，10代表JS播放器WAP端",
            "terminal": "观看终端 ，0代表iOSAPP，1代表AndroidAPP，2代表flash，3代表wap，4代表IOSSDK，5代表AndroidSDK，6代表小助手，7代表JS播放器WEB端，9代表微信小程序，10代表JS播放器WAP端",
        }