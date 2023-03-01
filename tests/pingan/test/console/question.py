#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.master.account import *
from app.preview.pingan.console.question import *
from utils.config_util import configUtil


accountObj = Account("test_pingan_api")
accountObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(accountObj.section, "console_token")
accountObj.setCommonData({'token': token})

testObj = Question("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'token': token})


# accessToken = accountObj.getAccessToken({
#     'from': 'js'
# })
# accessToken = accessToken.get("data").get("access_token")


create = {
    'q_id': 573482,
    'title': '测试添加',
    'description': 22,
    'from': 'js'
}
# testObj.create(create)

update = {
    'question_id': 573484,
    'description': '修改描述',
    'title': '修改名称',
}
# testObj.update(update)

detail = {
    "question_id": 573484
}
# testObj.detail(detail)

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
export = {
    'question_id': '573486',
    'il_id': '1100000614'
}
testObj.export(export);

