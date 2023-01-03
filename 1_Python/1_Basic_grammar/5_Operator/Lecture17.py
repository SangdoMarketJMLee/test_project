num1 = 10
num2 = 3
result = num1 / num2
print('num1: {}, num2: {}, result: {}'.format(num1,num2,result))

result = num1%num2
print('num1: {}, num2: {}, result: {}'.format(num1,num2,result))
result = num1 // num2
print('num1: {}, num2: {}, result: {}'.format(num1,num2,result))
result = divmod(num1,num2)
print('num1: {}, num2: {}, result: {}'.format(num1,num2,result))

allStuCnt = int(input('전체 학생 수 :'))
stuCntOfGroup = int(input('한 모둠 학생 수 :'))
groupCnt = allStuCnt // stuCntOfGroup
overStuCnt = allStuCnt % stuCntOfGroup
result = divmod(allStuCnt,stuCntOfGroup)
print('전체 학생 수 : {}'.format(allStuCnt))
print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
print('모둠 수 :{}'.format(groupCnt))
print('남은 학생 수 :{}'.format(overStuCnt))
print('모듬 수 : {}, 남은 학생 수:{}'.format(result[0],result[1]))

employee = 123
apple =4
result = divmod(employee, apple)

print('사과를 나누어 줄 수 있는 최대 직원 : {}'.format(result[0]))
print('남은 사과 개수 : {}'.format(result[1]))