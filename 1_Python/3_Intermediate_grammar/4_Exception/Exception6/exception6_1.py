num1 = int(input('inputNumber1 : '))
num2 = int(input('inputNumber2 : '))

try:
    print(f'num1/num2 : {num1/num2}')
except Exception as e:
    print('0으로 나눌 수 없습니다')
    print(f'exception: {e}')

print(f'num1+num2 : {num1+num2}')
print(f'num1-num2 : {num1-num2}')
print(f'num1*num2 : {num1*num2}')