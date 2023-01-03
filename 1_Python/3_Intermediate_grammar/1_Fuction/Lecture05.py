def calculator(n1,n2):
    result = n1 + n2
    return result

returnValue = calculator(10,20)
print(f'returnValue : {returnValue}')

def divideNumber(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'
returnValue1 = divideNumber(5)
print(f'returnValue1 : {returnValue1}')

def cmTmm(cm):
    result = cm * 10

    return result
length = float(input('길이(cm)입력 : '))
returnValue2 = cmTmm(length)
print(f'returnValue2 : {returnValue2}mm')

import random
def getOddRandomNumber():
    while True:
        rNum = random.randint(1,100)
        if rNum % 2 != 0:
            break

    return rNum

print(f'returnValue3 : {getOddRandomNumber()}')