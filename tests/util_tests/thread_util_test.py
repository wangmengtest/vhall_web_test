#!/usr/bin/env python
# encoding:utf8
import require
import time
from utils.time_util import timeUtil
from utils.thread_util import threadUtil


def sendMsg(process):
    timeUtil.sleep(0.5)
    print("%s-%i\r" % (process, process))


threadUtil.loadMore(sendMsg, 10)
threadUtil.loadMore(sendMsg, 10)
threadUtil.loadMore(sendMsg, 10)
threadUtil.exec()
