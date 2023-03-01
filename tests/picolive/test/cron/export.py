#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.cron.export import *

testObj = Export("test_pingan_api")
testObj.setDbSection("dev_picolive_db")


testObj.exportIndex()