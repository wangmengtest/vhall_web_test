#!/usr/bin/env python
# encoding:utf8
import require
from app.vhallyun.channel import *
from utils.time_util import timeUtil

# testObj = Channel("prod_pingan_vhallyun_api")
testObj = Channel("uat_herbalife_vhalyun_api")
# testObj = Channel("test_picolive_vhallyun_api")

getChannelUserOnLineCountParsm = {
    "channel_id": "ch_7516e747,ch_a8fb3c33,ch_454e2e50"
}
# testObj.getChannelUserOnLineCount(getChannelUserOnLineCountParsm)

getChannelConnectionCountParam = {
    "channel_id": "ch_7516e747,ch_a8fb3c33,ch_454e2e50"
}
# testObj.getChannelConnectionCount(getChannelConnectionCountParam)


getMessageState = {
    "channel_id": "ch_396d561d",
}
# testObj.getMessageState(getMessageState)

# result = testObj.messageLists({
#     "channel_id": "ch_c351862e",
#     "curr_page": "1",
#     "page_size": "10",
#     "msg_type": "all",
#     "order_by": "asc",
#     "filter_status": 0,
#     "audit_status": "all",
#     "start_time": "2021-01-01 00:00:00",
#     "end_time": "2021-10-30 23:59:59",
# })
# lists = result.get("data").get("list")
# print(len(lists))
#
# for i in lists:
#     # print(i)
#     print("%s %s %s" % (i.get('third_party_user_id'), i.get('data'), i.get("date_time")))

# testObj.getOnlineUserList({
#
# })

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
for i in range(3000):
    sendMessage["body"]['text_content'] = i
    testObj.sendMessage(sendMessage)
    timeUtil.sleep(0.01)

