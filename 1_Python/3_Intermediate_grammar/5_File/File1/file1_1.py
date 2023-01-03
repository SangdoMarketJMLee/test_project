# 시스템 시간과 일정을 텍스트 파일에 작성
import time

lt = time.localtime()
dateStr ='['+ str(lt.tm_year)+'년'+\
        str(lt.tm_mon) +'월'+\
        str(lt.tm_mday) + '일]'

todaySchedule = input('오늘 일정 : ')
file = open('../File1/test.txt','w')
file.write(dateStr + todaySchedule)
file.close()