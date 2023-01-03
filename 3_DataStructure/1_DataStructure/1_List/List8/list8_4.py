# 아래의 오늘 일정표에서 사용자가 입력한 일정을 삭제하는 프로그램

myList = ['마케팅 회의','회의록 정리','점심 약속','월간 업무 보고','치과 방문','마트 장보기']
print('myList : {}'.format(myList))
removeItem = input('삭제 대상 입력 : ')
myList.remove(removeItem)
print('일정 : {}'.format(myList))