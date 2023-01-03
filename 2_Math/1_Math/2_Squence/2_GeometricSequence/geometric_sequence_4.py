# 등비수열 공식을 활용하여 n 번째 항의 값을 출력하는 프로그램을 만들어라
inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('길이 입력 : '))
valueN =inputN1 *(inputR ** (inputN-1))
print("{}번쨰 항의 값: {}".format(inputN,valueN))

