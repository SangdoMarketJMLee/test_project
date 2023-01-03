# 다음 수열을 보고 n 번째 항의 값을 출력하는 프로그램을 만들어라

inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('길이 입력 : '))

valueN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        print("{}번쨰 항의 값: {}".format(n,valueN))
        n += 1
        continue
    valueN *= inputR
    print("{}번쨰 항의 값: {}".format(n,valueN))
    n += 1
print("{}번쨰 항의 값: {}".format(inputN,valueN))
