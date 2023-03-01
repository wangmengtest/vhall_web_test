#!/usr/bin/env python
# encoding:utf8
import os
from app.clitest.test import Test
testcases = [os.path.abspath(os.path.dirname(os.getcwd())) + '/auth.py', 'add.py', 'list.py']
testObj = Test()
testObj.testCase(testcases)
#children = subprocess.Popen(['python', testcase], shell=True, stdout = subprocess.PIPE)
#stdoutput = children.communicate()
#print(stdoutput)
