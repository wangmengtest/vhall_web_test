#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.pingan.master.account import *
from app.preview.pingan.master.question import *
from utils.config_util import configUtil


accountObj = Account("dev_pingan_api")
accountObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(accountObj.section, "console_token")
accountObj.setCommonData({'token': token})

testObj = Question("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
# vssToken = configUtil.get(testObj.section, "vss_token")
# testObj.setCommonData({'token': token, 'vss_token':vssToken})



# accessToken = accountObj.getAccessToken({
#     'from': 'js'
# })
# accessToken = accessToken.get("data").get("access_token")


create = {
    'room_id': 'lss_8ff68147',
    'title': '房间添加问卷',
    'description': '房间添加问卷描述',
    'question_id': 573486,
    'account_id': 80,
    'is_public': 1,
    'from': 'js'
}
# testObj.create(create)

update = {
    'question_id': 573486,
    'account_id': 80,
    'description': '修改描述',
    'title': '修改名称',
}
# testObj.update(update)

detail = {
    "question_id": 573486,
    'account_id': 80,
}
testObj.info(detail)

lists = {
    "keyword": "测试",
    "page": 1,
    "pagesize": 10,
}
# testObj.lists(lists)

delete = {
    'question_ids': '573482,573483'
}
# testObj.delete(delete)

repush = {
    "room_id": 'lss_9e7e2c45',
    'question_id': '579881',
    'account_id': '32',
    'from': 'js',
    'vss_token': 'access:6147b94a:c5fb7e75fc6f79d5',
}
testObj.repush(repush)