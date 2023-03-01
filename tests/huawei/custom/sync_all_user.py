#!/usr/bin/env python
# encoding:utf8

import require
from utils.request_util import requestUtil

host = "http://219.134.89.13:8082"

getAllUserAddress = "%s%s" % (host,"/wUser/selectUserAll")
getAllOrgAddress = "%s%s" % (host,"/wOrgOrgs/selectIOrgAll")


requestUtil.openDocHook("获取用户架构", sampleList=False)
getAllOrg = requestUtil.get(getAllOrgAddress, timeout=600)
print(len(getAllOrg))


# requestUtil.openDocHook("获取用户列表", sampleList=False)
# getAllUser = requestUtil.post(getAllUserAddress, timeout=60000)
# print(len(getAllUser))

