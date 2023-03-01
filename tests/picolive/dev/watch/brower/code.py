#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.code import *

testObj = Code("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

codeParam = {
    "phone": "18510248667",
    "area_code": "86",
}
testObj.send(codeParam)
