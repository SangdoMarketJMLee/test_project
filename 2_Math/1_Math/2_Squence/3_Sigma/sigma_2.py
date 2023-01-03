# n번쨰 항까지 합을 출력하는 프로그램
inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, valueN))
        n += 1
        continue

    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, valueN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))
