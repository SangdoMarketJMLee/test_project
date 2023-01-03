choose = int(input('언어 선택(choose your language): 1. 한국어 2.English' ))
if choose == 1:
    print('1. 샌드위치 \t 2. 햄버거 \t 3.쥬스 \t 4.커피 \t 5. 아이스크림')
if choose == 2:
    print('1. Sandwich \t 2. Hanburger \t 3.Juice \t 4.Coffee \t 5. Ice Cream')


maxAge = 100
age = int(input('나이 입력 :'))
hundred = maxAge - age
nowAge = 2022
print('{}년 ({}년후)에 100살'.format((nowAge+hundred),hundred))

import datetime

today = datetime.datetime.today()

myAge = input('나이 입력 : ')
if myAge.isdigit():
    afterAge = 100 - int(myAge)
    myHundred = today.year + afterAge

    print('{}년({}년후)에 100살!!'.format(myHundred, afterAge))
else:
    print('잘 못 입력했습니다.')
