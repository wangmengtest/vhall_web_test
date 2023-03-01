#!/usr/bin/env python
# encoding:utf8

"""
年级公共类
"""


class GradeUtil(object):
    # 初始化生成各种版本的年级信息
    gradeDict = {
        "1": 1,
        "1年": 1,
        "一": 1,
        "一年": 1,

        "2": 2,
        "2年": 2,
        "二": 2,
        "二年": 2,

        "3": 3,
        "3年": 3,
        "三": 3,
        "三年": 3,

        "4": 4,
        "4年": 4,
        "四": 4,
        "四年": 4,

        "5": 5,
        "5年": 5,
        "五": 5,
        "五年": 5,

        "6": 6,
        "6年": 6,
        "六": 6,
        "六年": 6,

        "7": 7,
        "7年": 7,
        "七": 7,
        "七年": 7,
        "初一": 7,

        "8": 8,
        "8年": 8,
        "八": 8,
        "八年": 8,
        "初二": 8,

        "9": 9,
        "9年": 9,
        "九": 9,
        "九年": 9,
        "初三": 9,

        "10": 10,
        "10年": 10,
        "十": 10,
        "十年": 10,
        "高一": 10,

        "11": 11,
        "11年": 11,
        "十一": 11,
        "十一年": 11,
        "高二": 11,

        "12": 12,
        "12年": 12,
        "十二": 12,
        "十二年": 12,
        "高三": 12,
    }

    def getStrIndex(self, strValue):
        reversedDict = reversed(self.gradeDict)

        for key in reversedDict:
            splitList = strValue.split(key)
            if len(splitList) == 2:
                return self.gradeDict[key]

        return False

    def getDbStrIndex(self, strValue):
        strIndex = self.getStrIndex(strValue)
        if not strIndex:
            return 0
        else:
            return strIndex


gradeUtil = GradeUtil()
# print(gradeUtil.getStrIndex("12年"))
