exampleScore = int(input('시험 성적 입력 : '))
grades = ''

if exampleScore >= 90:
    grades = 'A'
elif exampleScore >= 80:
    grades = 'B'
elif exampleScore >= 70:
    grades = 'C'
elif exampleScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {} \t 학점 : {}'.format(exampleScore,grades))

print('계절 : 봄, 여름, 가을, 겨울')
seasonStr = input('계절 입력 : ')

if seasonStr == '봄':
    print('{} : {}'.format('봄','Spring'))
elif seasonStr == '여름':
    print('{} : {}'.format('여름','Summer'))
elif seasonStr == '가을':
    print('{} : {}'.format('가을','Fall'))
elif seasonStr == '겨울':
    print('{} : {}'.format('겨울','Winter'))
else:
    print('검색할 수 없습니다.')

print('1.카페라떼(3.5) \t 2.에스프레스(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5.밀크티(4.3)')

userSelectNumber = int(input('메뉴 선택:'))
menu = ''
price = 0

if userSelectNumber == 1:
    menu = '카페라떼'
    price = 3500
elif userSelectNumber == 2:
    menu = '에스프레소'
    price = 3000
elif userSelectNumber == 3:
    menu = '아메리카노'
    price = 2000
elif userSelectNumber == 4:
    menu = '곡물라떼'
    price = 4000
elif userSelectNumber == 5:
    menu = '밀크티'
    price = 4300
print('-'*25)
print('메뉴 : {} \n가격 : {}'.format(menu,price))
print('-'*25)