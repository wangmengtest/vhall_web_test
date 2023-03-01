#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.cron.stat import *

testObj = Stat("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")


testObj.stat()