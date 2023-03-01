#!/usr/bin/env python
# encoding:utf8

import require
import datetime
from utils.config_util import configUtil
from utils.csv_read_util import CsvReadUtil
from utils.excel_write_util import ExcelWriteUtil


"""
读取禅道导出的数据报表
"""
# excelPath = configUtil.get('env', 'excel_path') + '/chandao/笔克v1.1版本.csv'
# writePath = configUtil.get('env', 'excel_path') + '/chandao/笔克v1.1版本.xlsx'

# excelPath = configUtil.get('env', 'excel_path') + '/chandao/笔克v1.0禅道.csv'
# writePath = configUtil.get('env', 'excel_path') + '/chandao/笔克1.0禅道.xlsx'

excelPath = configUtil.get('env', 'excel_path') + '/chandao/笔克v1.2版本.csv'
writePath = configUtil.get('env', 'excel_path') + '/chandao/笔克1.2禅道.xlsx'

excelObj = CsvReadUtil(excelPath, 'gbk')
# ['编号', '所属迭代', '所属模块', '相关需求', '任务名称', '任务描述', '任务类型', '优先级', '预计开始', '实际开始', '截止日期', '任务状态', '最初预计', '总消耗', '预计剩余', '抄送给', '进度', '由谁创建', '创建日期', '指派给', '指派日期', '由谁完成', '完成时间', '由谁取消', '取消时间', '由谁关闭', '关闭时间', '关闭原因', '最后修改', '最后修改日期', '附件']

excelData = excelObj.mapToIndex(2, [
    "id", "version", "module", "requirement", "name", "desc", "type", "-", "-", "start_time", "end_time", "status", "-", "used_time", "-", "-", "-", "created_user", "created_at", "user", "pointer", "pointer_time", "finish_user", "finish_time", "cancel_user", "cancel_time", "close_user", "close_time", "close_reason", "modify_user", "modify_time"
])

# 数据格式加工
for k, i in enumerate(excelData):
    excelData[k]['used_time'] = float(i['used_time'])

# 按分类入表
title = [
    '编号', '所属迭代', '所属模块', '相关需求', '任务名称', '任务描述', '任务类型', '-', '实际开始', '截止日期', '任务状态', '总消耗', '预计剩余', '创建日期', '指派给', '指派日期', '由谁完成', '完成时间', '由谁取消', '取消时间', '由谁关闭', '关闭时间', '关闭原因', '最后修改', '最后修改日期'
]
excelWriteObj = ExcelWriteUtil(writePath)

# 循环数据计算所有父级任务
parentIdList = []
lastChildId = 0
for key, value in enumerate(excelData):
    key = key + 1

    if value.get("name").find("[子]") >= 0:
        if key - lastChildId > 1:
            parentIdList.append(key - 2)

        lastChildId = key

# 获取最终没有父级信息
finalData = []
for key, value in enumerate(excelData):
    if key not in parentIdList:
        finalData.append(value)

del excelData

excelWriteObj.createSheet("全部")
excelWriteObj.setTitle(title)

for data in finalData:
    excelWriteObj.appendByList(list(data.values()))

# 数据分类
catList = {
    "设计": [],
    "开发": [],
    "BUG": [],
    "测试": [],
    "事务": [],
    "优化": [],
    "其他": [],
}

# 顺序需要动态慢慢优化至最优状态
descType = {
    "设计": "设计",
    "代码优化": "优化",
    "单元测试": "开发",
    "报错": "BUG",
    "排查": "BUG",
    "修复": "BUG",
    "bug": "BUG",
    "BUG": "BUG",
    "Bug": "BUG",
    "优化": "优化",
    "测试": "测试",
    "返讲": "事务",
    "反讲": "事务",
    "日会": "事务",
    "日清会": "事务",
    "事务": "事务",
    "研究": "事务",
    "异常": "异常",
    "验收": "事务",
    "检查": "事务",
    "解答": "事务",
    "讨论": "事务",
    "代码审核": "事务",
    "冒烟": "事务",
    "沟通": "事务",
    "UI": "设计",
    "ui": "设计",
    "sonar": "优化",
    "封装": "优化",
    "健康": "优化",
}

# 获取最终没有父级信息
for value in finalData:
    valueGotHome = False

    for i in descType:
        if value.get("type").find(i) >= 0:
            catList[descType[i]].append(value)
            valueGotHome = True
            break

    # 定制化分类
    if value.get("type").find("开发") >= 0 and value.get("desc").find("测试") >= 0:
        catList["开发"].append(value)
        valueGotHome = True

    if value.get("type").find("开发") >= 0 and value.get("desc").find("问题") >= 0:
        catList["BUG"].append(value)
        valueGotHome = True

    if not valueGotHome:
        for i in descType:
            if value.get("name").find(i) >= 0:
                catList[descType[i]].append(value)
                valueGotHome = True
                break

    if not valueGotHome:
        for i in descType:
            if value.get("desc").find(i) >= 0:
                catList[descType[i]].append(value)
                valueGotHome = True
                break

    if not valueGotHome:
        if value.get("type").find("开发") >= 0:
            catList["开发"].append(value)
        else:
            catList["其他"].append(value)

for i in catList:
    excelWriteObj.createSheet(i)
    excelWriteObj.setTitle(title)

    for data in catList[i]:
        excelWriteObj.appendByList(list(data.values()))

excelWriteObj.save()