#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.document import *
from utils.config_util import configUtil

testObj = Document("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


uploadParams = {
    'from': 'js',
}
documentUrl = configUtil.get('env', 'image_path')
testObj.documentUpload(uploadParams, documentUrl)
