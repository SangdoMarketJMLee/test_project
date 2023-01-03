# 최저 및 최고 점수를 삭제한 후 총점과 평균을 구하여라

scores = [9.5,8.9,9.2,9.8,8.8,9.0]
print('scores : {}'.format(scores))

scores.sort()
print('scores : {}'.format(scores))

scores.pop(0)

scores.pop(len(scores)-1)

print('scores : {}'.format(scores))

sum = 0
avg = 0

for score in scores:
    sum += score

avg = sum / len(scores)

print('총점 : %.2f'% sum)
print('평점 : %.2f'% avg)