#!/usr/bin/env python
# encoding:utf8

import subprocess
#os.system('ipconfig/all')
#通过os.system来执行py代码
import os
from app.clitest.test import Test

testcases = [os.path.abspath(os.path.dirname(os.getcwd())) + '/auth.py', 'upload.py', 'download.py']
testObj = Test()
testObj.testCase(testcases)
