num1 = 2
num2 = 3
result = num1 ** num2

print('num1 : {}'.format(num1))
print('num2 : {}'.format(num2))
print('result : {}'.format(result))

result = 2 ** (1/2)
print('2의 제곱근 %f' % result)
print('2의 제곱근 %.2f' % result)

result = 2 ** (1/3)
print('2의 3제곱근 %f' % result)
print('2의 3제곱근 %.2f' % result)

result = 2 ** (1/4)
print('2의 4제곱근 %f' % result)
print('2의 4제곱근 %.2f' % result)

import math

print('2의 제곱근 %f' % math.sqrt(2))
print('2의 제곱근 %.2f' % math.sqrt(2))

print('2의 3제곱근 %f' % math.sqrt(3))
print('2의 3제곱근 %.2f' % math.sqrt(3))

print('2의 4제곱근 %f' % math.sqrt(4))
print('2의 4제곱근 %.2f' % math.sqrt(4))

print('2의 3제곱 %f' % math.pow(2,3))
print('2의 3제곱 %f' % math.pow(3,4))

firstMonthMoney = 200
after12Month = ((firstMonthMoney*0.01)**12)*100
print('12개월 후 용돈 : %.f원'%after12Month)
after12Month = int(after12Month)
after12MonthFormat= format(after12Month,',')
print('12개월 후 용돈 : %s원' % after12MonthFormat)
