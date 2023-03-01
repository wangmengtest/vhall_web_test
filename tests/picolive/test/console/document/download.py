#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.document import *
from utils.config_util import configUtil

testObj = Document("test_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

downloadParam = {
    "document_id": "6d40e8aa",
}
testObj.download(downloadParam)
