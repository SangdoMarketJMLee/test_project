students = ['홍길동','박찬호','이용규','강호동','박승철','김지은']
print('students : {}'.format(students))

searchIdx = students.index('강호동')
print('searchIdx : {}'.format(searchIdx))


searchIdx = students.index('강호동',2,6)
print('searchIdx : {}'.format(searchIdx))