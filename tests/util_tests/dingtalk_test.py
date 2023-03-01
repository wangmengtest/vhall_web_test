#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require

from utils.cache_util import cacheUtil
from app.ali.dingtalk import Dingtalk

dingTalk = Dingtalk()
# result = dingTalk.getToken()

result = dingTalk.createGroup({
    "name": "消息通知-测试",
    "owner": "manager5875",
    "useridlist": ["manager5875"],
    "showHistoryType": 1,
    "searchable": 1,
    "validationType": 1,
    "mentionAllAuthority": 1
})

# 单步上传文档地址 https://developers.dingtalk.com/document/app/single-step-file-upload
# result = dingTalk.sendFileToGroup("/Users/nelsonking/Desktop/poetry_379_04_13.xlsx")
print(result)


