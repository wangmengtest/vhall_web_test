#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.cron.export import *

testObj = Export("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

exportIndex = {
    'ignore': '1',
    'id': '4',
}
testObj.exportIndex(exportIndex)