#!/usr/bin/env python
# encoding:utf8

import os
import sys

# 指定项目目录名称
rootName = "vhall_web_test"


# 获取当前地址
def currentPath(file=None):
    if file:
        return os.path.abspath(os.path.dirname(file))
    else:
        return os.path.abspath(os.path.dirname(__file__))


# 获取项目地址
def rootPath(appendPath=None):
    currentPathStr = currentPath()
    currentPathSplitList = currentPathStr.split(rootName)
    rootPathStr = currentPathSplitList[0] + rootName
    if appendPath:
        return rootPathStr + appendPath

    return rootPathStr


# 获取存储目录
def storagePath(appendPath=None):
    if appendPath:
        return rootPath("/storage") + appendPath

    return rootPath("/storage")


# 获取应用目录
def appPath(appendPath=None):
    if appendPath:
        return rootPath("/app") + appendPath

    return rootPath("/app")


# 获取配置目录
def configPath(appendPath=None):
    if appendPath:
        return rootPath("/config") + appendPath

    return rootPath("/config")


# 获取缓存目录
def cachePath(appendPath=None):
    if appendPath:
        return storagePath("/cache") + appendPath

    return storagePath("/cache")


# 获取日志目录
def logPath(appendPath=None):
    if appendPath:
        return storagePath("/log") + appendPath

    return storagePath("/log")


# 获取sql目录
def sqlPath(appendPath=None):
    if appendPath:
        return storagePath("/sql") + appendPath

    return storagePath("/sql")


# 获取sql目录
def excelPath(appendPath=None):
    if appendPath:
        return storagePath("/excel") + appendPath

    return storagePath("/excel")


if rootPath() not in sys.path:
    sys.path.append(rootPath())
