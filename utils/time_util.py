#!/usr/bin/env python
# encoding:utf8
import require
import time
import re

"""
公共时间处理函数 单例
"""


class TimeUtil(object):
    def __init__(self):
        self.timeInt = time.time()

    def updateTime(self):
        self.timeInt = time.time()

    # 秒级时间戳
    def getTimeIntSecond(self, update=True):
        if update:
            self.updateTime()

        return int(self.timeInt)

    # 毫秒级时间戳
    def getTimeIntMilliSecond(self, update=True):
        if update:
            self.updateTime()
        return print(int(round(self.timeInt * 1000)))

        # 微秒级时间戳

    def getTimeIntMicroSecond(self, update=True):
        if update:
            self.updateTime()
        return print(int(round(self.timeInt * 1000000)))

    def strtotime(self, string):
        """
        字符串转时间戳
        :param string:
        :return:
        """
        timeList = re.split("\D", string)
        if not len(timeList):
            print("时间格式不正确")
            exit()

        completeTimeList = []
        for i in range(6):
            if i < len(timeList):
                completeTimeList.append(timeList[i])
            else:
                if i <= 2:
                    completeTimeList.append("01")
                else:
                    completeTimeList.append("00")

        completeTimeStr = "%s-%s-%s %s:%s:%s" % (completeTimeList[0],
                                                 completeTimeList[1],
                                                 completeTimeList[2],
                                                 completeTimeList[3],
                                                 completeTimeList[4],
                                                 completeTimeList[5])

        return time.mktime(time.strptime(completeTimeStr, "%Y-%m-%d %H:%M:%S"))

    def format(self, timeInt, format="%Y-%m-%d %H:%M:%S"):
        """
        时间格式化
        :param format:
        :param timeInt:
        :return:
        """
        timeStruct = time.localtime(timeInt)
        return time.strftime(format, timeStruct)

    def timeIntOptionSecond(self, timeInt, second, option="add"):
        """
        时间戳追加时间
        :param timeInt:
        :param second:
        :param option:
        :return:
        """
        if option == "add":
            return timeInt + second
        else:
            return timeInt - second

    def timeStrOptionSecond(self, timeStr, second, option="add"):
        """
        时间字串戳追加时间
        :param timeStr:
        :param second:
        :param option:
        :return:
        """
        timeInt = self.strtotime(timeStr)
        if option == "add":
            finalTime = timeInt + second
        else:
            finalTime = timeInt - second

        return self.format(finalTime)

    def sleep(self, second):
        """
        睡眠
        :param second:
        :return:
        """
        time.sleep(second)


timeUtil = TimeUtil()
