#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

createRoomParam = {
    'name': '接口房间22',
    'begin_time': '2021-06-09 15:20:37',
    'welcome': '欢迎进入直播间',
    'tag_type': '6343',
    'display_style': 1,
    'risk_level': 'R1',
    'begin_time_stamp':  int(timeUtil.timeInt + 60),
    'introduction': '< p > 44 < / p >',
    'topics': '',
    'from': 'js',
    'en': 0,
    'image': '',
}
# testObj.roomCreate(createRoomParam)

roomUpdateStatusParam = {
    # "il_id": 1100000640,
    "il_id": 1100000553,
    "status": 0,
}

# testObj.roomUpdateStatus(roomUpdateStatusParam)



roomInfoParam = {
    "il_id": 1100000698
}
testObj.roomInfo(roomInfoParam)

roomListParam = {
    'page': 1,
    'keyword': '',
    'status': '',
    'orderby': '1',
    'platform': 'web',
}
# testObj.roomList(roomListParam)

# testObj.thirdartyTags()

tagListParam = {
    'type': 0
}
# testObj.tagList(tagListParam)

getInviteCodeParam = {
    "il_id": 1100000553,
}
# testObj.getInviteCode(getInviteCodeParam)

saveInviteCodeParam = {
    "il_id": 1100000646,
    "invite_code": ""
}
# testObj.saveInviteCode(saveInviteCodeParam)

pushStreamParams = {
    "il_id": 1100000794,
    "address": "rtmp://58.200.131.2:1935/livetv/cctv1",
}
# testObj.pushStream(pushStreamParams)

getPushStreamParam = {
    "il_id": 1100000696,
    "flush": 1,
}
# testObj.getPushStream(getPushStreamParam)
