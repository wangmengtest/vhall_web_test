#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.console.document import *
from utils.config_util import configUtil

testObj = Document("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'from': 'js',
    'document_id':'1b14429a',
    #'ext': 'txt,ppt'
}
documentUrl = configUtil.get('env', 'image_path')
testObj.getInfo(uploadParams)
