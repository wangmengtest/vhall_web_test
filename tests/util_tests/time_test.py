#设a为字符串
import require
from utils.time_util import timeUtil
import time
a = "2011-09-28 10:00:59"
timeInt = timeUtil.strtotime(a)
print(timeInt)
addNewYearInt = timeUtil.timeIntOptionSecond(timeInt, 3600 * 24 * 365)
print(addNewYearInt)

timeStr = timeUtil.format(timeInt)
addNewYearStr = timeUtil.timeStrOptionSecond(timeStr, 3600 * 24 * 365)

#中间过程，一般都需要将字符串转化为时间数组
result = time.strptime(a,'%Y-%m-%d %H:%M:%S')
print(result)
# >>time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50, tm_sec=0, tm_wday=1, tm_yday=270, tm_isdst=-1)

#将"2011-09-28 10:00:00"转化为时间戳
result = time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
print(result)
# >>1317091800.0

#将时间戳转化为localtime
x = time.localtime(1317091800.0)
result = time.strftime('%Y-%m-%d %H:%M:%S',x)
print(result)
# >>2011-09-27 10:50:00

# 获得今天的年月日
today =  time.strftime("%Y%m%d", time.localtime())
print(today)