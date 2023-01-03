origin = [1,1,2,2,2,8]
cur = list(map(int,input('숫자를 입력해주세요 :').split()))
for i in range(6):
    print(origin[i]-cur[i],end=" ")