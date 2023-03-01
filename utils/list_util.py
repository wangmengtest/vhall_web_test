#!/usr/bin/env python
# encoding:utf8
import json
import prettyprinter
import require
import hashlib
import dict_hash
from utils.string_util import stringUtil

"""
公共字符串类 列表
"""


class ListUtil(object):
    history = {}

    #  列表搜索
    def index(self, data, index):
        if index in data:
            return data.index(index)
        return -1

    # 字典列表通过指定键值对，转换为单字典
    def listDictAssignKeyValue(self, data, key, value):
        tmpDict = {}
        for listDict in data:
            if not isinstance(listDict, dict):
                print(listDict)
                print("转换的数据结构不对")
                exit()

            if (key not in listDict) or (value not in listDict):
                print(listDict)
                print("键 %s 或 值 %s 不存在" % (key, value))
                exit()

            tmpDict[listDict[key]] = listDict[value]

        return tmpDict

    # 清理缓存
    def removeCache(self, data, searchData):
        index = "%s:%s" % (id(data), id(searchData))

        if index in self.history:
            del self.history[index]

    # 通过指定的列表字典，在字典列表中寻找是否含有
    def listDictSearchOneDict(self, data, searchData):
        if not data or not isinstance(data, list):
            return False

        for searchKey in searchData:
            if not data[0][searchKey]:
                return False

            if isinstance(data[0][searchKey], int):
                searchData[searchKey] = int(searchData[searchKey])

        for i in data:
            if not searchData.items() - i.items():
                return i

        return False

    # 通过指定的列表字典，在字典列表中寻找是否含有
    def listDictSearchListDict(self, data, searchData):
        result = []

        if not data or not isinstance(data, list):
            return result

        for searchKey in searchData:
            if not data[0][searchKey]:
                return result

            if isinstance(data[0][searchKey], int):
                searchData[searchKey] = int(searchData[searchKey])

        for i in data:
            if not searchData.items() - i.items():
                result.append(i)

        return result

    # 字典列表通过指定键，转换为单列表
    def listDictAssignKey(self, data, key, toTuple=None):
        tmpList = []
        for listDict in data:
            if not isinstance(listDict, dict):
                print(listDict)
                print("转换的数据结构不对")
                exit()

            if key not in listDict:
                print(listDict)
                print("键 %s 不存在" % key)
                exit()

            value = listDict[key]
            if value not in tmpList:
                tmpList.append(value)

        if toTuple:
            return tuple(tmpList)
        else:
            return tmpList


listUtil = ListUtil()
