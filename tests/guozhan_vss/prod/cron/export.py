#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.cron.export import *

testObj = Export("prod_pingan_api")
testObj.setDbSection("dev_csces_db")


testObj.exportIndex()