#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.cron.stat import *

testObj = Stat("test_pingan_api")
testObj.setDbSection("dev_picolive_db")


testObj.stat()