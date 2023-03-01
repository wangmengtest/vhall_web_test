#!/usr/bin/env python
# encoding:utf8
import require
from app.vps.qa import *
from utils.config_util import configUtil

testObj = Qa("vps")

num = {
    'webinar_id': 'lss_c8164815',
}
testObj.num(num)

lists = {
}
# testObj.lists(lists)