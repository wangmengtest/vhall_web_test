#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.time_util import timeUtil
from utils.request_util import requestUtil

# requestUtil
# result = requestUtil.post("http://d.csces.com/console/org/list?token=cd277dc153c6634e", {}, {})

# print(result)

# result = requestUtil.post("https://pingan.vhallyun.com/openapi/room/attends",
#           {
#               "end_date": "2021/09/26",
#               "il_id": "1100002236",
#               "page": "1",
#               "per_page": "100",
#               "sign": "253e8b6d4dd21dce422fdbcce45fc358",
#               "signed_at": "1632623500",
#               "start_date": "2021/09/06",
#               "type": "1"
#           }
# )
# print(len(result.get('data')))

# for i in range(20):
#     requestUtil.post("https://pingan.vhallyun.com/log/collect", {
#         "name": "gaoyan",
#         "age": "18",
#         "i": i
#     }, {})

# for i in range(20):
#     requestUtil.post("http://d.pingan.com/log/collect", {
#         "name": "gaoyan",
#         "age": "18",
#         "i": i
#     }, {})

# result = requestUtil.post("http://wlf2021.wlaforum.com/api/wla-cms-srv/restDict/queryTress",
#           {
#           }
# )
# print(result)
# for i in range(100):
#     result = requestUtil.exec("https://wlf2021.wlaforum.com/api/wla-cms-srv/agenda/filters", 'post', {}, {'main': 0, 'month': "9", 'year': "2021"})
#     if not result.get('data'):
#         print(result)
#         exit()
#

# requestUtil.post("http://share.cscecsteel.com:8082/wOrgOrgs/selectSubordinatePkOrgByPkOrg/0001A110000000002ZF0", {
#     "token": "de09b828f263d6bc",
# })
#
# requestUtil.upload("")

sendUserGiftParams = {
    "channel": "WEIXIN",
    "numbers": "1",
    "service_code": "QR_PAY",
    "gift_id": "8",
    "room_id": "lss_2303f30e",
    "channel_id": "ch_f7b61a55",
    "nick_name": "测试1",
    "name": "飞机",
    "image_url": "https://nuohe-test-1253248467.cos.ap-beijing.myqcloud.com/vss/0ba95e95090240e8a8b950bf7a9b1268.png",
    "vss_token": "access:GUSIiWRX:6ede921668ac7206",
    "from": "js",
    "token": "24eeac55e0247eff"
}

# sendUserGiftHeaderParams = {
#     "vsstoken": "access:GUSIiWRX:6ede921668ac7206",
#     "token": "24eeac55e0247eff"
# }
#
# for i in range(1000):
# requestUtil.post("https://t-nuohe-api.vhallyun.com/v4/gift/send", sendUserGiftParams, sendUserGiftHeaderParams)
#     timeUtil.sleep(0.5)

# for i in range(100000):
#     result = requestUtil.get("http://localhost:1122/room/watch?source=1&il_id=9907")
#     print(result)


# requestUtil.postJson("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f5b10898-02e4-43f1-b6c5-03389737b512", {
#         "msgtype": "text",
#         "text": {
#             "content": "hello world!!"
#         }
# })

# curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f5b10898-02e4-43f1-b6c5-03389737b512' \
#      -H 'Content-Type: application/json' \
#         -d '
# {
#     "msgtype": "text",
#     "text": {
#         "content": "hello world"
#     }
# }'

# for i in range(1000):
requestUtil.post("https://api.vhallyun.com/sdk/v2/message/send", {
    "client": "pc_browser",
    "app_id": "876202fd",
    "third_party_user_id": 4038620,
    "access_token": "access:876202fd:bf008d25aa888b25",
    "package_check": "package_check",
    "type": "service_im",
    "channel_id": "ch_421854f7",
    "no_audit": 0,
    "body": {
        "type":"text",
        "text_content":"gggg"
    },
    "context": {
        "nickname":"1851024",
        "avatar":"",
        "role_name":2,
        "replyMsg":{},
        "atList":[],
        "roleNameText":{}
    }
})
    # timeUtil.sleep(0.5)

