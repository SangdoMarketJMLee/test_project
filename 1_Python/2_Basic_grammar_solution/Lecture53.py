import random
comNum = random.randint(1,2)
userSelect = int(input('홀/짝 선택: 1. 홀 \t 2. 짝 : '))

if comNum == 1 and userSelect == 1:
    print('빙고!! 홀수!!')
elif comNum == 2 and userSelect == 2:
    print('빙고!! 짝수!!')
elif comNum == 1 and userSelect == 2:
    print('실패!! 홀수!!')
elif comNum == 2 and userSelect == 1:
    print('실패!! 짝수!!')

print('-'*25)

comNum = random.randint(1,3)
userSelect = int(input('가위, 바위, 보 선택: 1. 가위 \t 2. 바위 \t 3. 보: '))

if (comNum == 1 and userSelect == 2) or \
        (comNum == 2 and userSelect ==3) or \
        (comNum ==3 and userSelect ==1):
    print('컴퓨터 패 , 유저 승')
elif comNum == userSelect:
    print('무승부')
else:
    print('컴퓨터 승, 유저 패')

print('컴퓨터 : {}, 유저 : {}'.format(comNum, userSelect))
