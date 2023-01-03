busA = 15
busB = 13
busC = 8
totalMin = 17 * 60
for i in range(totalMin + 1):
    if i < 20 or i > (totalMin - 60):
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!',end='')
            hour = 6 +i // 60
            min = i % 60
            print('\t {} : {}'.format(hour,min))
    else:
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!',end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t {} : {}'.format(hour, min))
        elif i % busA == 0 and i % busC == 0:
            print('busA와 busC 동시 정차!!',end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t {} : {}'.format(hour, min))
        elif i % busB == 0 and i % busC == 0:
            print('busB와 busC 동시 정차!!',end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t {} : {}'.format(hour, min))