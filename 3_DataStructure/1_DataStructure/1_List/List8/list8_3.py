students = ['홍길동','박찬호','이용규','강호동','박승철','김지은','강호동']
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))

while '강호동' in students:
    students.remove('강호동')

print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))

