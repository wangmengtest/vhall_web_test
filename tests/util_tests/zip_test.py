#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.config_util import configUtil
from utils.zip_util import zipUtil

sslPathDir = configUtil.get("env", "ssl_path")
sslFilePathDir = sslPathDir + "/ssl"


result = zipUtil.unzip_list(sslPathDir + "/zip_test.zip", 3)
nameList = []
for path in result:
    if path.find("api") > -1:
        nameList.append(path)

zipUtil.unzip_file(sslPathDir + "/zip_test.zip", sslFilePathDir, nameList)
print(nameList)
exit()

for file in os.listdir(sslPathDir):
    if file.find("zip") > -1:
        filePath = "%s/%s" % (sslPathDir, file)
        # result = zipUtil.unzip_file(filePath, sslFilePathDir)
        result = zipUtil.unzip_list(filePath)
        # print(file)
        # print(result)
        exit()
# print(sslPathDir)
# print(sslFilePathDir)








