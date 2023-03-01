#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.console.document import *
from utils.config_util import configUtil

testObj = Document("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'from': 'js',
}
testObj.documentUpload(uploadParams, "/Users/nelsonking/Desktop/新建 PPT 演示文稿.ppt")
