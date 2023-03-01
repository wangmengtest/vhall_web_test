#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.channel import *

# testObj = Channel("test_pingan_vhallyun_api")
# testObj = Channel("test_wlaforum_vhallyun_api")
testObj = Channel("test_xiaomi_vhallyun_api")

getChannelUserOnLineCountParam = {
    "channel_id": "ch_7516e747,ch_a8fb3c33,ch_454e2e50"
}
# testObj.getChannelUserOnLineCount(getChannelUserOnLineCountParam)

getChannelConnectionCountParam = {
    "channel_id": "ch_7516e747,ch_a8fb3c33,ch_454e2e50"
}
# testObj.getChannelConnectionCount(getChannelConnectionCountParam)

checkUserOnlineParams = {
    'third_party_user_ids': '80',
    'channel_id': 'ch_55f0fdf8',
}
# testObj.checkUserOnline(checkUserOnlineParams)

# testObj.getOnlineUserList({
#     "channel_id": "ch_8I1d5cuj",
#     "curr_page": 0,
#     "page_size": 1000,
# })


testObj.getMessageState({
    # "channel_id": "ch_bsf87E5K",
    "channel_id": "ch_9zESBtm4",
})