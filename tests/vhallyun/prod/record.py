#!/usr/bin/env python
# encoding:utf8
import require
import json
from app.vhallyun.record import *
from utils.time_util import timeUtil

testObj = Record("prod_wlaforum_vhallyun_api")

transCodeParams = {
    'vod_id': "835e9a94",
    'quality': '360p,480p,720p',
}
# result = testObj.transCode(transCodeParams)


pageEach = True
recordId = "1b181be9"

# while pageEach:
pos = 0
limit = 100
getRecordJoinInfoParam = {
    'record_id': recordId,
    'pos': pos,
    'limit': limit,
    'start_time': '2020-11-01 17:34:00',
    'end_time': '2021-11-01 19:10:00',
}
# testObj.getRecordJoinInfo(getRecordJoinInfoParam)


videoEdit = {
    'vod_id': "6476efbd",
    'cut_sections': json.dumps({})
}
# testObj.videoEdit(videoEdit)


createRecord={
    'stream_id': 'lss_bde933f1',
    'start_time': '2021-11-03 09:00:00',
    'end_time': '2021-11-03 12:30:00'
}
# testObj.createRecord(createRecord)

transCode = {
    "vod_id": "1037edc6",
    "quality": "360p,480p,720p",
}
testObj.transCode(transCode)