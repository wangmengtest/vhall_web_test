#!/usr/bin/env python
# encoding:utf8

import time
import require
from app.vhallyun.record import *
from utils.db_util import DBUtil
from app.ali.dingtalk import Dingtalk
from utils.time_util import timeUtil

testRecordObj = Record("az_test_pingan_vhallyun_api")
prodRecordObj = Record("az_prod_pingan_vhallyun_api")
dbUtil = DBUtil("az_delete_db")
dingtalk = Dingtalk()

testAppId = "20541bf7"
prodAppId = "bca53047"


# 处理返回值，加工处理成功和为未成功的数据
def delResponse(data, processList):
    if "data" in data \
            and "code" in data \
            and data.get("code") == 200:

        deletedVod = data.get('data').get("deleted_vod_list")
        failList = list(set(processList).difference(set(deletedVod)))
    else:
        deletedVod = []
        failList = [processList]

    for vod_id in deletedVod:
        dbUtil.composeUpdateExec("vod_list", {"status": 1}, {"vod_id": vod_id})

    for vod_id in failList:
        dbUtil.composeUpdateExec("vod_list", {"status": 2}, {"vod_id": vod_id})

    print("exec @ %s" % timeUtil.format(time.time()))


finished = False
second = 0

while not finished:
    vodList = dbUtil.select("select * from vod_list where status = 0 limit 10")

    testVodList = []
    prodVodList = []
    vodProcessList = []

    for vodInfo in vodList:
        vodProcessList.append(vodInfo.get("vod_id"))

        if vodInfo.get('app_id') == testAppId:
            testVodList.append(vodInfo.get("vod_id"))

        if vodInfo.get('app_id') == prodAppId:
            prodVodList.append(vodInfo.get("vod_id"))

    if not prodVodList and not testVodList:
        finished = True
        print("finished @ %s" % timeUtil.format(time.time()))

    if testVodList:
        requestData = {
            'vod_id': ",".join(testVodList)
        }
        result = testRecordObj.recordDelete(requestData)
        delResponse(result, vodProcessList)

    if prodVodList:
        requestData = {
            'vod_id': ",".join(prodVodList)
        }
        result = prodRecordObj.recordDelete(requestData)
        delResponse(result, vodProcessList)

    time.sleep(1)
    second += 1

    # 每小时投递消息
    if second % 3600 == 0:
        remain = dbUtil.selectOne("select count(*) as num from vod_list where status = 0")
        dingtalk.send("exec @ %s remain %s" % (timeUtil.format(time.time()), remain.get('num')))
