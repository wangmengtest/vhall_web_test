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

fileObj = FileUtil("./yapi-api.json", 'w+')

# print(projectObj.icon("统计"))
# print(projectObj.icon("二维码"))
# print(projectObj.icon("红包"))
# print(projectObj.icon("标签"))
# exit()

"""
YAPI 分组同步功能
"""
# 用户登录
# http://chandao.ops.vhall.com:3000/api/user/login_by_ldap

userName = "yan2.gao"
password = "Nelsonking7.22"
# 拷贝哪个项目
sourceGroup = 1077

# 往哪个项目上拷贝
targetGroup = 1337

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
    projectName = projectIdList[projectId]
    if projectName.find("工厂相关") > -1:
        continue

    # 获取项目信息
    exportParam = {
        "type": "json",
        "pid": projectId,
        "status": "all",
        "isWiki": "false",
    }

    projectJson = projectObj.export(exportParam)

    # 创建
    addParam = {
        "basepath": "",
        "color": projectObj.color(),
        "group_id": targetGroup,
        "icon": projectObj.icon(projectName),
        "name": projectName,
        "project_type": "private",
    }

    fileObj.append(stringUtil.jsonObjectFormat(addParam))    
    projectInfo = projectObj.add(addParam)
    projectId = projectInfo.get("data").get("_id")

    # 获取分组菜单列表
    getMenuParam = {
        'project_id': projectId,
    }
    menuInfo = projectObj.getMenu(getMenuParam)
    menuInfo = menuInfo.get("data")

    menuDict = {}
    for menu in menuInfo:
        menuDict[menu.get("name")] = menu.get("_id")


    # 获取元数据所有分类
    for menuObj in projectJson:
        menuName = menuObj.get("name")
        if menuName in menuDict:
            menuId = menuDict[menuName]
        else:
            # 创建菜单
            addMenuParam = {
                "desc": menuName,
                "name": menuName,
                "project_id": projectId
            }
            menuAddInfo = projectObj.addCat(addMenuParam)    
            menuId = menuAddInfo.get("data").get("_id")

        #  循环添加项目
        for apiObj in menuObj.get("list"):
            apiObj["project_id"] = projectId    
            apiObj["catid"] = menuId
            apiObj["catname"] = "公共分类"

            if apiObj["api_opened"]:
                apiObj["api_opened"] =  "true"
            else:
                apiObj["api_opened"] =  "false"

            if apiObj["req_body_is_json_schema"]:
                apiObj["req_body_is_json_schema"] =  "true"
            else:
                apiObj["req_body_is_json_schema"] =  "false"

            if apiObj["res_body_is_json_schema"]:
                apiObj["res_body_is_json_schema"] =  "true"
            else:
                apiObj["res_body_is_json_schema"] =  "false"                
        

            apiObj["dataSync"] = "merge"
            jsonString = stringUtil.jsonObjectFormat(apiObj)
            fileObj.append(jsonString)

            projectObj.importJson(apiObj)

print(projectIdList)    
