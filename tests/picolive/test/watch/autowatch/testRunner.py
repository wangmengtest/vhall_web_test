#!/usr/bin/env python
# encoding:utf8

#from app.preview.picolive.console.auth import *
#from utils.config_util import configUtil
import unittest
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath + '111111')
print(f"{os.getcwd()}" + '2222222')
sys.path.append(f"{os.getcwd()}")
from app.clitest.test import Test
from app.clitest.TestRunnerHtmls import *

class TestWatch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        print("execute tearDownClass")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    def test_one(self):
        print('execute test_one')
        self.assertTrue('FOO'.isupper())

    def test_two(self):
        print('execute test_two')

    def test_three(self):
        print('execute test_thre')

    def test_autowatch(self):
        sys.path.append(f"{os.getcwd()}")
        testcases = [
            curPath + '/auth.py',
            #curPath + '/watch.py'
        ]
        testObj = Test()
        testObj.testCase(testcases)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Test3是要测试的类名，test_one是要执行的测试方法
    suite.addTest(TestWatch("test_one"))
    suite.addTest(TestWatch("test_two"))
    suite.addTest(TestWatch("test_three"))
    suite.addTest(TestWatch("test_autowatch"))
    # 实践中发现执行时的当前路径，不一定是此文件所在的文件夹，所以使用绝对路径
    print(f"{os.getcwd()}")
    filename = os.getcwd() + '/storage/log/unittest.html'
    fb = open(filename, 'wb')
    #obj = HTMLTestRunner()
    runner = HTMLTestRunner(stream=fb, title="测试HTMLTestRunner", description="测试啊1")
    runner.run(suite)
    fb.close()
