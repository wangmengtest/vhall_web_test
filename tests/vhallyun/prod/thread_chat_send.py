#!/usr/bin/env python
# encoding:utf8
import require
from app.vhallyun.channel import *
from utils.time_util import timeUtil
from utils.thread_util import threadUtil

testObj = Channel("uat_herbalife_vhalyun_api")

sendMessage={
    "third_party_user_id": "4038621",
    "channel_id": "ch_421854f7",
    "type": "service_im",
    "client": "pc_browser",
    "body": {
        "type": "text",
        "text_content": ""
    },
}


def sendMsg(process):
    for i in range(10):
        sendMessage["body"]["text_content"] = "%s-%i" % (process, i)
        testObj.sendMessage(sendMessage)
        timeUtil.sleep(1)


threadUtil.loadMore(sendMsg, 10)
threadUtil.exec()