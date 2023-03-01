#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.cron.export import *

testObj = Export("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")


testObj.exportIndex()