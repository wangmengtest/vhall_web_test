#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.message import *
import json
from utils.time_util import timeUtil
from utils.request_util import requestUtil

# testObj = Message("test_picolive_vhallyun_api")
testObj = Message("uat_herbalife_vhalyun_api")

createLivePullStreamConfigParam = {
    "channel_id":"ch_JaSr0LoB",
    "curr_page":1,
    "page_size":20,
    "msg_type":"text,image",
    "order_by":"asc",
    "filter_status":0,
    "audit_status":"all",
    "start_time":"2021-07-14 17:48:38",
    "end_time":"2021-07-14 17:48:40",
}

# testObj.lists(createLivePullStreamConfigParam)

for i in range(1000):
    # sendHostParams = {
    #     "app_id": "876202fd",
    #     "client": "pc_browser",
    #     "third_party_user_id": 204884,
    #     "type": "service_im",
    #     "channel_id": "ch_efe81f4a",
    #     "access_token": "access:876202fd:49ca8047265460cd",
    #     "package_check": "package_check",
    #     "no_audit": 1,
    #     "body": json.dumps({"type": "text", "text_content": "exec number %s" % timeUtil.getTimeIntSecond()}),
    #     "context": json.dumps({
    #         "nickname": "超级权限", "avatar": "", "role_name": 1, "replyMsg": {}, "atList": [],
    #         "roleNameText": {"text": "主持人", "type": "host"}
    #     })
    # }

    sendUserParams = {
        "app_id": "GUSIiWRX",
        "client": "pc_browser",
        "third_party_user_id": "672",
        "access_token": "access:GUSIiWRX:0b75de8132413526",
        "package_check": "package_check",
        "type": "service_im",
        "channel_id": "ch_f7b61a55",
        "no_audit": 0,
        "body": json.dumps({"type":"text","text_content":"user send time %s" % timeUtil.getTimeIntSecond()}),
        "context": json.dumps({"nickname":"18510248667","avatar":"","role_name":2,"replyMsg":{},"atList":[],"roleNameText":{}}),
    }

    testObj.sdkSend(sendUserParams)
    timeUtil.sleep(2)
