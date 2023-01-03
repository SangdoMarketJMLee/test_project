kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
math = int(input('수학 점수 : '))
science = int(input('과학 점수 : '))
history = int(input('역사 점수 : '))

total = (kor + eng + math + science + history)
average = int(total/5)

korAvg = 85; engAvg = 82; mathAvg = 89; scienceAvg = 75; historyAvg = 94
totalAvg = (korAvg + engAvg + mathAvg + scienceAvg + historyAvg)
averageAvg = int(totalAvg/5)
totalDeviation = total - totalAvg
averageDeviation = average - averageAvg
korDeviation = kor - korAvg
engDeviation = eng - engAvg
mathDeviation = math - mathAvg
scienceDeviation = science - scienceAvg
historyDeviation = history - historyAvg
print('-'*30)
print('총점 : {}({}), 평균 : {}({})'.format(total,totalDeviation,average,averageDeviation))
print('국어 : {}({}), 영어 : {}({}), 수학 : {}({}), 과학 : {}({}), 국사 : {}({})'.format(kor, korDeviation, eng, engDeviation, math, mathDeviation, science, scienceDeviation, history, historyDeviation))
print('-'*30)
if korDeviation > 0:
    print('국어 편차 :{}({})'.format('+'*korDeviation,korDeviation))
else:
    print('국어 편차 :{}({})'.format('-' * abs(korDeviation), korDeviation))
if engDeviation > 0:
    print('영어 편차 :{}({})'.format('+'*engDeviation,engDeviation))
else:
    print('영어 편차 :{}({})'.format('-' * abs(engDeviation), engDeviation))
if mathDeviation > 0:
    print('수학 편차 :{}({})'.format('+'*mathDeviation,mathDeviation))
else:
    print('수학 편차 :{}({})'.format('-' * abs(mathDeviation), mathDeviation))
if scienceDeviation > 0:
    print('과학 편차 :{}({})'.format('+'*scienceDeviation,scienceDeviation))
else:
    print('과학 편차 :{}({})'.format('-' * abs(scienceDeviation), scienceDeviation))
if historyDeviation > 0:
    print('국사 편차 :{}({})'.format('+'*historyDeviation,historyDeviation))
else:
    print('국사 편차 :{}({})'.format('-' * abs(historyDeviation), historyDeviation))
if totalDeviation > 0:
    print('총점 편차 :{}({})'.format('+'*totalDeviation,totalDeviation))
else:
    print('총점 편차 :{}({})'.format('-' * abs(totalDeviation), totalDeviation))
if averageDeviation > 0:
    print('평균 편차 :{}({})'.format('+'*averageDeviation,averageDeviation))
else:
    print('평균 편차 :{}({})'.format('-' * abs(averageDeviation), averageDeviation))

print('-'*30)