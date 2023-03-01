#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.console.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

createRoomParam = {
    'name': '创建测试%s' % int(timeUtil.timeInt),
    'begin_time': timeUtil.format(timeUtil.timeInt),
    'welcome': '欢迎进入直播间',
    'tag_type': '3',
    'display_style': 1,
    'risk_level': 'R1',
    'begin_time_stamp':  int(timeUtil.timeInt + 60),
    'introduction': '< p > 44 < / p >',
    'topics': '',
    'from': 'js',
    'en': 0,
    'image': '',
    'stream_type': 2,
}
# testObj.roomCreate(createRoomParam)

roomUpdateStatusParam = {
    # "il_id": 1100000640,
    "il_id": 1100000553,
    "status": 0,
}

# testObj.roomUpdateStatus(roomUpdateStatusParam)



roomInfoParam = {
    "il_id": 1100000619
}
# testObj.roomInfo(roomInfoParam)

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

saveBullet = {
    "il_id": 1100000619,
    "bullet": 1,
    "bullet_btn": 1,
}
# testObj.saveBullet(saveBullet)

setLiveRecord = {
    "il_id": "1100000619",
    "vod_id": "w",
}
testObj.setLiveRecord(setLiveRecord)

liveRecordInfo = {
     "il_id": "1100000619",
}
testObj.liveRecordInfo(liveRecordInfo)

rePushLiveRecord = {
    "il_id": "1100000619",
}
# testObj.rePushLiveRecord(rePushLiveRecord)

deleteLiveRecord = {
    "il_id": "1100000619",
}
# testObj.deleteLiveRecord(deleteLiveRecord)