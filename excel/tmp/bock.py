#!/usr/bin/env python
# encoding:utf8

import require
import datetime
from utils.config_util import configUtil
from utils.excel_read_util import ExcelReadUtil
from utils.file_util import FileUtil
from utils.db_util import DBUtil
from utils.list_util import listUtil


"""
读取禅道导出的数据报表
"""
excelPath = configUtil.get('env', 'excel_path') + '/【截至0120】Final汇总版110596-年会弹幕敏感词.xlsx'

fileObj = FileUtil("./block.sql", "w+")
dbUtil  = DBUtil('dev_common_db')

excelObj = ExcelReadUtil(excelPath)
excelData = excelObj.mapToIndex(1, ['word'])

excelData = listUtil.listDictAssignKey(excelData, 'word')
print(excelData)
exit()


sql = dbUtil.composeInsert('sensitives', excelData)

fileObj.append(sql)
print("success")
exit()



for key, value in enumerate(excelData):
    sql = dbUtil.composeInsert('sensitives', {
        'word': value.get("block")
    })

    fileObj.append(sql)

print("success")