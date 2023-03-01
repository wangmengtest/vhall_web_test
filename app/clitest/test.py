#!/usr/bin/env python
# encoding:utf8
import subprocess

class Test():
    def testCase(self, testcases):
        success = 0;
        failProcess = []
        for testcase in testcases:
            with subprocess.Popen(['python', testcase], shell=True, stdout=subprocess.PIPE, encoding="utf-8") as output:
                cliOutput = output.stdout.readlines()
                if not cliOutput:
                    break
            for output in cliOutput:
                output = output.decode("utf8","ignore")
                if '请求结果为' in output:
                    if '"code": 200' in output:
                        print('success')
                        success += 1
                    else:
                        print('failed')
                        failProcess.append(testcase + output)
        print('执行' + str(len(testcases)) + '个用例 失败' + str(len(testcases) - success) + '个')
        print('成功' + str(success) + '个')
        print('失败' + str(len(testcases) - success) + '个')
        print('失败用例结果集:')
        for fail in failProcess:
            print(fail)
        return
