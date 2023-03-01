#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.cron.stat import *

testObj = Stat("prod_pingan_api")
testObj.setDbSection("dev_csces_db")


testObj.stat()