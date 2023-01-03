choose = int(input('업종 선택(1. 가정용\t 2.대중탕용\t 3.공업용) : '))
useAmount = int(input('사용량 입력 : '))

print('='*25)
print('상수도 요금표')
print('-'*25)
if choose == 1:
    if useAmount > 0:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount,useAmount*540))
elif choose == 2:
    if useAmount < 50:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount, useAmount * 820))
    elif useAmount >50 and useAmount <300:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount, useAmount * 1920))
    elif useAmount > 300:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount, useAmount * 2400))
elif choose == 3:
    if useAmount < 500:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount, useAmount * 240))
    elif useAmount > 500:
        print('사용량 : 요금 \n{}    : {}'.format(useAmount, useAmount * 470))
print('='*25)