# 사용자로부터 숫자 5개를 입력 받아 짝수, 홀수, 실수로 구분해서 각각을 리스트에 저장하는 프로그램

evenList = []; oddList = []; floatList = []

n = 1
while n<6:
    try:
        num = float(input('inputNumber : '))
    except:
        print('exception raise')
        print('inputNumber again')
        continue
    else:
        if num - int(num) != 0:
            print('floatNumber!')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('evenNumber!')
                evenList.append(int(num))
            else:
                print('oddNumber')
                oddList.append(int(num))
    n += 1

print(f'evenList : {evenList}')
print(f'oddList : {oddList}')
print(f'floatList : {floatList}')