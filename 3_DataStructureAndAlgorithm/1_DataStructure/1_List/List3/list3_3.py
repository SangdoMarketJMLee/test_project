# 5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 학생과 짝수(0포함)인 학생를 구분해서 인덱스와 학생 이름을 출력
# for 문으로 출력
students = ['김성예','신경도','박기준','최승철','황동석']

for i in range(5):
    if i % 2 == 0:
        print('인덱스 짝수 : students[{}] : {}'.format(i,students[i]))
    else:
        print('인덱스 홀수 : students[{}] : {}'.format(i, students[i]))
