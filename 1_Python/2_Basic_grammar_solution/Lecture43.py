circle_r = int(input('반지름(cm) 입력 : '))
pi = 3.14
circle_area = (circle_r*circle_r)*pi
circumference_circle = 2*pi*circle_r
print('원의 넓이 %d' % circle_area)
print('원의 둘레 %d' % circumference_circle)
print('원의 넓이 %.1f' % circle_area)
print('원의 둘레 %.1f' % circumference_circle)
print('원의 넓이 %.3f' % circle_area)
print('원의 둘레 %.3f' % circumference_circle)

name = input('이름 입력 :')
mail = input('메일 입력 :')
id = input('아이디 입력:')
pw = input('비밀번호 입력:')
citizenNum1 = input('주민 번호 앞자리 입력 :')
citizenNum2 = input('주민 번호 뒤자리 입력 :')
address = input('주소 입력 :')


print('-'*25)
print('이름 : {}'.format(name))
print('메일 : {}'.format(mail))
print('아이디 : {}'.format(id))
pwStar = '*'*len(pw)
print('비밀번호 : {}'.format(pwStar))
citizenNum2Star = citizenNum2[0]+ ('*'*6)
print('주민번호 : {} - {} '.format(citizenNum1,citizenNum2Star))
print('주소 : {}'.format(address))
print('-'*25)