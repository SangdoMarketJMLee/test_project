greatATCnt = int(input('GreatA 톱니수 입력: '))
greatBTCnt = int(input('GreatB 톱니수 입력: '))

gearA = 0
gearB = 0
leastNum = 0
flag = True
while flag:
    if gearA != 0:
        if gearA != leastNum:
            gearA += greatATCnt
        else:
            flag = False
    else:
        gearA += greatATCnt

    if gearB != 0 and gearB % greatATCnt == 0:
        leastNum = gearB
    else:
        gearB += greatBTCnt

    print('gearA : {}, gearB: {}'.format(gearA,gearB))

print('최초 만나는 톱니수(최소공배수): {}톱니'.format(leastNum))
print('gearA 회전수 : {} 회전'.format(int(leastNum/greatATCnt)))
print('gearV 회전수 : {} 회전'.format(int(leastNum/greatBTCnt)))