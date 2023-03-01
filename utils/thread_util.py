#!/usr/bin/env python
# encoding:utf8
import require
import threading
import multiprocessing


class ThreadUtil(object):
    handle = {}
    processList = []

    def loadMore(self, func, processNum):
        self.processList.append({
            "func": func,
            'processNum': processNum,
        })

        if processNum > multiprocessing.cpu_count():
            print("The number of CPU is:" + str(multiprocessing.cpu_count()))
            print("you processNum out of cpu number")

    def exec(self):
        for processList in self.processList:
            func = processList['func']
            processNum = processList['processNum']

            for i in range(processNum):
                self.handle[i] = threading.Thread(target=func, args=(i,))
                self.handle[i].start()

        print("thread num: %s" % threading.active_count())

        print(self.handle)
        print("\r")


threadUtil = ThreadUtil()
