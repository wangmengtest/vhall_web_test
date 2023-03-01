#!/usr/bin/env python
# encoding:utf8

import json
import require
import unicodedata
import prettyprinter

"""
公共字符串类 单例
"""


class StringUtil(object):
    # 格式化输出 Json 对象
    def jsonObjectFormatPrint(self, content):
        try:
            print(json.dumps(content, sort_keys=True, indent=4, ensure_ascii=False))
        except Exception as e:
            print(e)

    # 格式化输出 Json 字符串
    def jsonStringFormatPrint(self, content):
        try:
            content = json.loads(content)
            print(self.jsonObjectFormatPrint(content))
        except Exception as e:
            print(e)

    # 格式化 Json 对象
    def jsonObjectFormat(self, content, beauty=True):
        try:
            if beauty:
                return json.dumps(content, sort_keys=True, indent=4, ensure_ascii=False)
            else:
                return json.dumps(content, ensure_ascii=False)
        except Exception as e:
            print(e)

    # 格式化 Json 字符串
    def jsonStringFormat(self, content, beauty=True):
        try:
            content = json.loads(content)
            return self.jsonObjectFormat(content, beauty)
        except Exception as e:
            print(e)

    # 去掉首位空白
    def trim(s):
        if not isinstance(s, str):
            raise ('not suportting')
        if s == ' ':
            return ' '
        else:
            while s[:1] == ' ':  # 使用while循环每次去掉首部的一个空字符
                s = s[1:]
            while s[-1:] == ' ':  # 使用while循环每次去掉尾部的一个空字符
                s = s[:-1]
        return s

    # 通过索引数字获取大写ABC
    def getBigAbcFromIndex(self, index):
        return self.getIntToAscII(65 + index)

    # 通过索引数字获取小写abc
    def getSmallAbcFromIndex(self, index):
        return self.getIntToAscII(97 + index)

    # 获取acs码的对应数字
    def getAscIIToInt(self, string):
        return ord(string)

    # 数字转asc码
    def getIntToAscII(self, number):
        return chr(number)

    # 结构字符串转字典
    def structStringToDict(self, string, newline="\n", split="\t"):
        dictData = {}
        headerArray = string.split(newline)

        for i in headerArray:
            keyValue = i.split(split)
            if len(keyValue) == 2:
                dictData[keyValue[0]] = str(keyValue[1])
        return dictData

    # 英文标点转中文标点
    def enToCnPunctuation(self, strValue):
        table = {ord(f): ord(t) for f, t in zip(
            u"!\"#$%&'()*+,-./:;<=>?@\^_`{|}~",
            u"！“#￥%&‘（）*+，—。/：；《=》？@\^ `{|}~")}

        strValue = str(strValue).translate(table)
        strValue = strValue.replace("…", "……")

        return strValue

    # 中文标点转英文标点
    def cnToEnPunctuation(self, strValue):
        table = {ord(f): ord(t) for f, t in zip(
            u"！“#￥%&‘（）*+，—。/：；《=》？@\^ `{|}~",
            u"!\"#$%&'()*+,-./:;<=>?@\^_`{|}~")}

        strValue = str(strValue).translate(table)
        strValue = strValue.replace("……", "…")

        return strValue

    def underLineToHump(self, string, firstBig=False):
        functionName = ""
        useUpper = firstBig

        for i in range(0, len(string)):
            if string[i] in ["_", "-"]:
                useUpper = True
            else:
                if useUpper:
                    functionName += str.upper(string[i])
                    useUpper = False
                else:
                    functionName += string[i]

        return functionName

    def isNumber(self, s):
        if not s:
            return False

        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def isFloat(self, s):
        if self.isNumber(s):
            if str(s).find(".") > 0:
                return True
            return False
        return False

    def toNumber(self, s):
        if self.isNumber(s):
            return unicodedata.numeric(s)
        return False


stringUtil = StringUtil()
