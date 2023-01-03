num1 = 9
num2 = 3
result = num1+num2
print(f'result: {result}')

fNum1 = 3.14
fNum2 = 0.12
fResult = fNum1+fNum2
print(f'fResult : {fResult}')
print('fResult : %.2f' % fResult)

result = num1+fNum2
print(f'result " {result}')

str1 ='good'
str2 =' '
str3 ='morning'
result = str1+str2+str3
print(f'result : {result}')

kor = int(input('국어 점수 :'))
eng = int(input('영어 점수 :'))
mat = int(input('수학 점수 :'))

total = kor+eng+mat

print('국어 점수 {}'.format(kor))
print('영어 점수 {}'.format(eng))
print('수학 점수 {}'.format(mat))
print('합계 {}'.format(total))

num1 = 10
num2 = 20
result = num1 - num2
print(f'num1 : {num1}')
print(f'num2 : {num2}')
print(f'result : {result}')

fNum1 = 3.14
fNum2 = 0.14
result = fNum1 - fNum2
print(f'fNum1 : {fNum1}')
print(f'fNum2 : {fNum2}')
print(f'result : {result}')
print(f'type(result) : {type(result)}')

partTimeMoney = int(input('알바비 입력 : '))
cardMoney = int(input('카드 값: '))
result = partTimeMoney - cardMoney
print('partTimeMoney : {}원'.format(partTimeMoney))
print('cardMoney : {}원'.format(cardMoney))
print('남은돈 : {}원'.format(result))