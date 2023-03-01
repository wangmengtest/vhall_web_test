#!/usr/bin/env python
# encoding:utf8

import require
import datetime
from utils.excel_write_util import ExcelWriteUtil
from utils.list_util import listUtil
from utils.db_util import DBUtil
from utils.time_util import timeUtil

"""
导出如下活动信息字段
活动ID	活动标题	创建时间	活动开始时间	活动实际开始时间	活动结束时间	是否删除活动，0否1是	是否为点播，0否1是	直播观看次数	直播观看人数	回放观看次数	回放观看人数	直播时长[分]	直播场次	直播观看最高并发数	移动端观看人数	pc端观看人数	累计观众人数	累计观看次数	观看时长[分](直播,回放)	点赞数	评论数
"""

host = "127.0.0.1"
port = 3306
user = "root"
password = "gaoyansing"
database = "pingan"
excelSavePath = "/Users/nelsonking/Desktop/vhall/excel/room_stat_info.xlsx"

# dbUtil = DBUtil("dev_pingan_db")
dbUtil = DBUtil(host=host, port=port, user=user, password=password, database=database)
excelObj = ExcelWriteUtil(excelSavePath)
excelObj.setTitle([
    '活动ID',
    '活动标题',
    '创建时间',
    '活动开始时间',
    '活动实际开始时间',
    '活动结束时间',
    '是否删除活动',
    '是否为点播',
    '直播观看次数',
    '直播观看人数',
    '回放观看次数',
    '回放观看人数',
    '直播时长[分]',
    '直播观看最高并发数',
    '移动端观看人数',
    'pc端观看人数',
    '累计观众人数',
    '累计观看次数',
    '观看时长[分](直播,回放)',
    '点赞数',
    '评论数'
])

# 查询所有房间信息
listRooms = dbUtil.select("""
SELECT
	rooms.il_id,
	rooms.`subject`,
	rooms.created_at,
	rooms.begin_live_time,
	rooms.end_live_time,
	if(rooms.deleted_at is null, '否', '是') as 'is_deleted',
    if(live_type=3,'是','否') as 'is_record',
	rooms.`like`,
	channel_id
FROM
	rooms
""")
print("room select finish")

roomUvAttends = dbUtil.select("""
SELECT
	count(distinct watch_account_id) AS num,
	il_id 
FROM
	room_attends 
WHERE
	terminal IN ( 0, 1, 4, 5, 7) 
GROUP BY
	il_id
""")
roomUvAttends = listUtil.listDictAssignKeyValue(roomUvAttends, 'il_id', 'num')
print("roomUvAttends select finish")

roomMobileAttends = dbUtil.select("""
SELECT
	count(*) AS num,
	il_id 
FROM
	room_attends 
WHERE
	terminal IN ( 0, 1, 4, 5 ) 
GROUP BY
	il_id
""")
roomMobileAttends = listUtil.listDictAssignKeyValue(roomMobileAttends, 'il_id', 'num')
print("roomMobileAttends select finish")

roomPcAttends = dbUtil.select("""
SELECT
	count(*) AS num,
	il_id 
FROM
	room_attends 
WHERE
	terminal = 7
GROUP BY
	il_id
""")
roomPcAttends = listUtil.listDictAssignKeyValue(roomPcAttends, 'il_id', 'num')
print("roomPcAttends select finish")

roomDurationAttends = dbUtil.select("""
SELECT
	sum(room_attends.duration) as duration,
	il_id 
FROM
	room_attends 
GROUP BY
	il_id
""")
roomDurationAttends = listUtil.listDictAssignKeyValue(roomDurationAttends, 'il_id', 'duration')
print("roomDurationAttends select finish")

roomMaxConnect = dbUtil.select("""
SELECT
	max(room_connect_counts.count) AS num,
	il_id 
FROM
	room_connect_counts 
GROUP BY
	il_id
""")
roomMaxConnect = listUtil.listDictAssignKeyValue(roomMaxConnect, 'il_id', 'num')
print("roomMaxConnect select finish")

recordUvAttends = dbUtil.select("""
SELECT
	count(distinct watch_account_id) AS num,
	il_id 
FROM
	record_attends 
WHERE
	terminal IN ( 0, 1, 4, 5, 7) 
GROUP BY
	il_id
""")
recordUvAttends = listUtil.listDictAssignKeyValue(recordUvAttends, 'il_id', 'num')
print("recordUvAttends select finish")

recordMobileAttends = dbUtil.select("""
SELECT
	count(*) AS num,
	il_id 
FROM
	record_attends 
WHERE
	terminal IN ( 0, 1, 4, 5 ) 
GROUP BY
	il_id
""")
recordMobileAttends = listUtil.listDictAssignKeyValue(recordMobileAttends, 'il_id', 'num')
print("recordMobileAttends select finish")

recordPcAttends = dbUtil.select("""
SELECT
	count(*) AS num,
	il_id 
FROM
	record_attends 
WHERE
	terminal = 7
GROUP BY
	il_id
""")
recordPcAttends = listUtil.listDictAssignKeyValue(recordPcAttends, 'il_id', 'num')
print("recordPcAttends select finish")

recordDurationAttends = dbUtil.select("""
SELECT
	sum(record_attends.duration) as duration,
	il_id 
FROM
	record_attends 
GROUP BY
	il_id
""")
recordDurationAttends = listUtil.listDictAssignKeyValue(recordDurationAttends, 'il_id', 'duration')
print("recordDurationAttends select finish")

channelCount = dbUtil.select("""
SELECT
	channel_id,
	count(*) as num
FROM
	chat_send_msg
GROUP BY
    channel_id
""")
channelCount = listUtil.listDictAssignKeyValue(channelCount, 'channel_id', 'num')
print("channelCount select finish")

for room in listRooms:
    roomId = room.get("il_id")
    channelId = room.get("channel_id")

    roomUvAttendNum = 0
    if roomId in roomUvAttends:
        roomUvAttendNum = roomUvAttends[roomId]

    roomPcAttendNum = 0
    if roomId in roomPcAttends:
        roomPcAttendNum = roomPcAttends[roomId]

    roomMobileAttendNum = 0
    if roomId in roomMobileAttends:
        roomMobileAttendNum = roomMobileAttends[roomId]

    roomDuration = 0
    if roomId in roomDurationAttends:
        roomDuration = roomDurationAttends[roomId]

    roomMaxConnectNum = 0
    if roomId in roomMaxConnect:
        roomMaxConnectNum = roomMaxConnect[roomId]

    recordUvAttendNum = 0
    if roomId in recordUvAttends:
        recordUvAttendNum = recordUvAttends[roomId]

    recordPcAttendNum = 0
    if roomId in recordPcAttends:
        recordPcAttendNum = recordPcAttends[roomId]

    recordMobileAttendNum = 0
    if roomId in recordMobileAttends:
        recordMobileAttendNum = recordMobileAttends[roomId]

    recordDuration = 0
    if roomId in recordDurationAttends:
        recordDuration = recordDurationAttends[roomId]

    roomCheatNum = 0
    if channelId in channelCount:
        roomCheatNum = channelCount[channelId]

    endTime = 0
    endLiveTime = room.get('end_live_time')
    if endLiveTime and isinstance(endLiveTime, datetime.datetime):
        endTime = timeUtil.strtotime(room.get('end_live_time').strftime("%Y-%m-%d %H:%M:%S"))

    startTime = 0
    beginLiveTime = room.get('begin_live_time')
    if beginLiveTime and isinstance(beginLiveTime, datetime.datetime):
        startTime = timeUtil.strtotime(room.get('begin_live_time').strftime("%Y-%m-%d %H:%M:%S"))

    liveDuration = 0
    if endTime - startTime:
        liveDuration = round((endTime - startTime) / 60, 2)

    data = [
        room.get('il_id'),
        room.get('subject'),
        room.get('created_at').strftime("%Y-%m-%d %H:%M:%S"),
        room.get('start_time') or '',
        room.get('begin_live_time') or '',
        room.get('end_live_time') or '',
        room.get('is_deleted'),
        room.get('is_record'),
        roomPcAttendNum + roomMobileAttendNum,
        roomUvAttendNum,
        recordPcAttendNum + recordMobileAttendNum,
        recordUvAttendNum,
        liveDuration,
        roomMaxConnectNum,
        roomMobileAttendNum + recordMobileAttendNum,
        roomPcAttendNum + recordPcAttendNum,
        roomUvAttendNum + recordUvAttendNum,
        roomPcAttendNum + roomMobileAttendNum + recordPcAttendNum + recordMobileAttendNum,
        round((roomDuration + recordDuration) / 60, 2),
        room.get('like'),
        roomCheatNum,
    ]
    excelObj.appendByList(data)

excelObj.save()
print("excel success")
