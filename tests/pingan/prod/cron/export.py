#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.cron.export import *

testObj = Export("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")


testObj.exportIndex()