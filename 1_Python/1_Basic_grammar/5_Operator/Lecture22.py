print('{} and {} : {}'.format(True,True,(True and True)))
print('{} and {} : {}'.format(True,True,(False and True)))
print('{} and {} : {}'.format(True,True,(True and False)))
print('{} and {} : {}'.format(True,True,(False and False)))

print('{} or {} : {}'.format(True,True,(True or True)))
print('{} or {} : {}'.format(True,True,(False or True)))
print('{} or {} : {}'.format(True,True,(True or False)))
print('{} or {} : {}'.format(True,True,(False or False)))

print('not {} : {}'.format(True,( not True)))
print('not {} : {}'.format(False,(not False)))

age = int(input('나이 입력 :'))
vaccine = (age < 20) or (age >= 65)
print('age: {}, result :{}'.format(age, vaccine))

kor = int(input('국어 점수 : '))
korScore = kor >= 60
eng = int(input('영어 점수 : '))
engScore = eng >= 60
math = int(input('수학 점수 : '))
mathScore = math >= 60

avg = float(kor+eng+math)/3
avgScore = avg >=70
pass_or_fail = (korScore and engScore and mathScore) and avgScore
print('평균 : {}, 결과 : {}'.format(avg,avgScore))
print('국어 :{}, 결과 : {}'.format(kor,korScore))
print('영어 :{}, 결과 : {}'.format(eng,engScore))
print('수학 :{}, 결과 : {}'.format(math,mathScore))
print('과락 결과: {}'.format(pass_or_fail))
print('최종 결과: {}'.format(pass_or_fail))



