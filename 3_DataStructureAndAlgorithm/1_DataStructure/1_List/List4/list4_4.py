# 아래 표와 리스트를 이용해서 학급별 학생 수와 전체 학생수 그리고 평균학생 수 출력해보자
studentsCnts =[[1,18],[2,19],[3,23],[4,21],[5,20],[6,22],[7,17]]

sum = 0
avg = 0

for classNo, cnt in studentsCnts:
    print('{}학급 학생수 : {}'.format(classNo,cnt))
    sum += cnt

print('전체 학생 수 : {}'.format(sum))
print('전체 학생 수 : {}'.format(sum/len(studentsCnts)))
