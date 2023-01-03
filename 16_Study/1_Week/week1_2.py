student = []
for i in range(1,31):
    student.append(i)

for no in range(28):
    student.remove(int(input('출석번호를 입력하세요 : ')))

print(*student,sep='\n')
