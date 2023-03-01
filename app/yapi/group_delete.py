#!/usr/bin/env python
# encoding:utf8

import require
import json
from utils.log_util import logUtil
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.db_util import DBUtil
from utils.time_util import timeUtil
from hashlib import md5
from app.yapi.user import userObj
from app.yapi.project import projectObj
from utils.cache_util import cacheUtil
from utils.file_util import FileUtil
from utils.string_util import stringUtil

"""
YAPI 分组同步功能
"""
# 用户登录
# http://chandao.ops.vhall.com:3000/api/user/login_by_ldap

userName = "yan2.gao"
password = "Nelsonking7.22"
sourceGroup = 1337

userCookie = "yapi_user_cookie_%s" % userName
cookie = cacheUtil.get(userCookie)

if not cookie:
    print("重新获取cookie %s" % userName)

    loginParams = {
        "email": userName,
        "password": password
    }
    userObj.login(loginParams)

    # 获取登录凭据
    cookie = userObj.getCookie()

    cacheUtil.set(userCookie, cookie, 3600)

projectObj.setCookie(cookie)
userObj.setCookie(cookie)

# 获取当前分组 （用户输入）
listParam = {
    "group_id": sourceGroup,
    "page": 1,
    "limit": 1000,
}

# 获取分组的所有项目
# http://chandao.ops.vhall.com:3000/api/project/list?group_id=1147&page=1&limit=10
projectList = projectObj.list(listParam)
projectList = projectList.get("data").get("list")

# 项目ID列表
projectIdList = {}

for project in projectList:
    projectIdList[project.get("_id")] = project.get("name")

for projectId in projectIdList.keys():
    # 删除项目
    delParam = {
        "id": projectId,
    }

    projectJson = projectObj.delete(delParam)
