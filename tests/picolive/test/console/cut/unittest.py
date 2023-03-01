#!/usr/bin/env python
# encoding:utf8
import os
from app.clitest.test import Test
testcases = [os.path.abspath(os.path.dirname(os.getcwd())) + '/auth.py', 'list.py', 'merge-record.py', 'save-record.py', 'get-vod-info.py']
testObj = Test()
testObj.testCase(testcases)
