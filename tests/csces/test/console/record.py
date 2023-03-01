#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.console.record import *
from utils.config_util import configUtil

testObj = Record("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordListParam = {
    "il_id": 1100000608,
    "page": 1,
    "pagesize": 100,
}
# testObj.recordList(recordListParam)


relatedListParam = {
    "il_id": 1100000592,
    "page": 1,
    "pagesize": 100,
}
# testObj.relatedList(relatedListParam)

saveRelatedVodParam = {
    "show_vod": 1,
    "il_id": 1100000610
}
# testObj.saveRelatedVod(saveRelatedVodParam)
downloadParam = {
    "record_id": "3f66fc5d"
}
testObj.download(downloadParam)