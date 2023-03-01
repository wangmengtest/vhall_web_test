#!/usr/bin/env python
# encoding:utf8

import require
import datetime
import random
from utils.file_util import FileUtil
from utils.db_util import DBUtil
from utils.config_util import configUtil
from utils.csv_read_util import CsvReadUtil
from utils.excel_write_util import ExcelWriteUtil


"""
加工昵称
"""

dbUtil = DBUtil("dev_pingan_db")

excelPath = configUtil.get('env', 'excel_path') + '/nickname.csv'
nickNameSql = configUtil.get('env', 'excel_path') + '/nickname.sql'


fileObj = FileUtil(nickNameSql, 'w+')

excelObj = CsvReadUtil(excelPath)

excelData = excelObj.mapToIndex(2, [
    "id", "userId", "nickName"
])

random.shuffle(excelData)

# 循环数据计算所有父级任务
NickNameList = []
index = 9999


for key, value in enumerate(excelData):
    index += 1
    insertData = {
        'id': index,
        'nickname': value.get("nickName")
    }
    sql = dbUtil.composeInsert('users', insertData)
    fileObj.append(sql)

