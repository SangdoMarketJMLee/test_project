minScore = 60
scores = [
    ['국어',58],
    ['영어',77],
    ['수학',89],
    ['과학',99],
    ['국사',50]
]
for subject, score in scores:
    if score < minScore: continue
    print('과락 과목 : {}, 점수 : {}'.format(subject,score))