#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.cron.stat import *

testObj = Stat("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")


testObj.stat()