#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.pingan.admin.document import *
from utils.config_util import configUtil

testObj = Document("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})


lists = {
    'keyword': '规范'
}
# testObj.lists(lists)

delete = {
    'document_ids': '7f6e0de0,81213574'
}
# testObj.delete(delete)

download = {
    'document_id': '097841db'
}
testObj.download(download)
