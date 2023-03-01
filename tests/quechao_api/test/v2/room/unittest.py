#!/usr/bin/env python
# encoding:utf8
import os
from app.clitest.test import Test
testcases = ['auth.py', 'create.py', 'update.py', 'list.py']
testObj = Test()
testObj.testCase(testcases)
