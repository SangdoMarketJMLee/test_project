
a = input('메시지 입력 : ')
print(len(a))

b = " 파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 \
인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. 파이썬이라는 이름은 귀도가 좋아하는 \
코미디 〈Monty Python's Flying Circus〉에서 따온 것이다 "
print(b.find('객체지향'))

width = int(input('가로 길이 입력 :'))
height = int(input('세로 길이 입력 :'))

triangle = float((width*height)/2)
square = float(width*height)
print('삼각형 넓이 %.6f'%triangle)
print('사각형 넓이 %.6f'%square)
print('삼각형 넓이 %.2f'%triangle)
print('사각형 넓이 %.2f'%square)