# 사용자로부터 숫자 5개를 입력 받아 짝수, 홀수, 실수와 입력한 모든 데이터를 각각 출력하는 프로그램

evenList = []; oddList = []; floatList = []; dataList = []

n = 1
while n<6:
    try:
        data = input('inputNumber : ')
        floatNum = float(data)
    except:
        print('exception raise')
        print('inputNumber again')
        continue
    else:
        if floatNum - int(floatNum) != 0:
            print('floatNumber!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('evenNumber!')
                evenList.append(int(floatNum))
            else:
                print('oddNumber')
                oddList.append(int(floatNum))
        n += 1
    finally:
        dataList.append(data)

print(f'evenList : {evenList}')
print(f'oddList : {oddList}')
print(f'floatList : {floatList}')
print(f'dataList : {dataList}')