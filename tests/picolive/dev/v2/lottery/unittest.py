#!/usr/bin/env python
# encoding:utf8
import os
from app.clitest.test import Test
testcases = [
    os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))) + '/console/login/auth.py',
    os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))) + '/api/inav/get.py',
    'import-user.py',
    'count.py',
    'search.py',
    'search.py',
    'add.py',
    'end.py',
    'publish.py'
]
testObj = Test()
testObj.testCase(testcases)
