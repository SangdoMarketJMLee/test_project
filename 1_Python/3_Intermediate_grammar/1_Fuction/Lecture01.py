'''
함수란
- 함수 -> 기능
- 파이썬의 함수는 수학의 함수와 동일
input -> 함수 -> output
1,2 -> x + y ->  3
'''
def addFun(x,y):
    return x + y

print(addFun(3,4))
'''
내장 함수, 사용자 함수
- 함수는 파이썬에서 기본으로 제공하는 내장 함수와 사용자가 직접 선언하는 사용자 함수 가 있다
'''

print('Hello python!!')

str = input()
print(f'str: {str}')
print(f'str length: {len(str)}')

numbers = [1, 2, 3, 4, 5]
numbers.sort()
print(f'number : {numbers}')

numbers.reverse()
print(f'numbers : {numbers}')

numbers.clear()
print(f'numbers : {numbers}')

def printUserName(name):
    print(f'{name} 고객님, 안녕하세요')

printUserName('이재명')

def addCal(n1, n2):
    result = n1 + n2
    print(f'n1+n2 = {result}')
addCal(3,5)
'''
함수의 사용 이유
기능을 재사용하기 위해서
'''
def addCal1():
    n1 = int(input('n1 입력 :'))
    n2 = int(input('n2 입력 :'))
    print(f'n1+n2 = {n1 + n2}')

addCal1()
# n1 = int(input('n1 입력 : '))
# n2 = int(input('n2 입력 : '))
# print(f'n1 + n2 = {n1 + n2}')
#
# n1 = int(input('n1 입력 : '))
# n2 = int(input('n2 입력 : '))
# print(f'n1 + n2 = {n1 + n2}')
#
# n1 = int(input('n1 입력 : '))
# n2 = int(input('n2 입력 : '))
# print(f'n1 + n2 = {n1 + n2}')
#
# n1 = int(input('n1 입력 : '))
# n2 = int(input('n2 입력 : '))
# print(f'n1 + n2 = {n1 + n2}')
#
# n1 = int(input('n1 입력 : '))
# n2 = int(input('n2 입력 : '))
# print(f'n1 + n2 = {n1 + n2}')

