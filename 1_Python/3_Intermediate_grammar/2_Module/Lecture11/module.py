import Calculator

Calculator.add(10, 20)
Calculator.sub(10, 20)
Calculator.mul(10, 20)
Calculator.div(10, 20)

import Calculator as cal
cal.add(10,20)
cal.sub(10,20)
cal.mul(10,20)
cal.div(10,20)

from Calculator import add
from Calculator import sub

add(10,20)
sub(10,20)

import Scores as sc

korScore = int(input('국어 점수 입력 :'))
engScore = int(input('영어 점수 입력 :'))
matScore = int(input('수학 점수 입력 :'))

sc.addScore(korScore)
sc.addScore(engScore)
sc.addScore(matScore)

print(sc.getScore())
print(sc.getTotalScore())
print(sc.getAvgScore())