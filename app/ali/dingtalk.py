#!/usr/bin/env python
# encoding:utf8

import json
import os
import sys
import require
import requests
from utils.cache_util import cacheUtil
from utils.request_util import requestUtil
from utils.config_util import configUtil

"""
钉钉消息API
"""


class Dingtalk(object):
    # 接口域名
    apiDomain = "https://oapi.dingtalk.com/"

    def __init__(self):
        self.appKey = configUtil.get("dingtalk", "appKey")
        self.appSecret = configUtil.get("dingtalk", "appSecret")
        self.groupId = configUtil.get("dingtalk", "groupId")

    # 发送消息
    def send(self, message):
        return self.sendToGroup(message)

    def getUrl(self, apiPath, withToken=True):
        if withToken:
            return "%s%s?access_token=%s" % (self.apiDomain, apiPath, self.getToken())
        else:
            return "%s%s" % (self.apiDomain, apiPath)    

    # 获取 dingtalk token
    def getToken(self):
        cacheKey = "dingtalk_token"
        cacheToken = cacheUtil.get(cacheKey)
        if cacheToken:
            return cacheToken
        else:
            apiPath = "gettoken"
            requestData = {
                "appkey": self.appKey,
                "appsecret": self.appSecret
            }
            
            result = requestUtil.get(self.getUrl(apiPath, False), requestData, {})
            token = result.get("access_token")
            cacheUtil.set(cacheKey, token, 3600 * 2)

            return token

    # 发送消息到组
    def sendToGroup(self, message):
        apiPath = "chat/send"
        requestData = {
            "chatid": self.groupId,
            "msg": {
                "msgtype": "text",
                "text": {
                    "content": message
                }
            }
        }

        return requestUtil.postJson(self.getUrl(apiPath), requestData)

    # 发送消息到组
    def sendFileToGroup(self, path):
        apiPath = "chat/send"
        requestData = {
            "chatid": self.groupId,
            "msg": {
                "msgtype": "file",
                "file": {
                    'media_id': self.getMediaId(path)
                }  
            }
        }
        print(requestData)

        return requestUtil.postJson(self.getUrl(apiPath), requestData)        

    # 获取上传文件ID
    def getMediaId(self, path):
        apiPath = "media/upload"

        requestData = {
            'access_token': self.getToken(),
            'type': 'file'
        }

        response = requestUtil.upload(self.getUrl(apiPath), path, requestData)
        json = response.json()

        if not json.get("media_id"):
            print(json.get("errmsg"))
            exit()

        return json["media_id"]   

    # 创建组
    def createGroup(self, data):
        if not data:
            data = {}

        apiPath = "chat/create"
        return requestUtil.postJson(self.getUrl(apiPath), data)
