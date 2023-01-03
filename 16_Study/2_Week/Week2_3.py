N, K = map(int, input().split())
coinArr = []
for i in range(N):
    coinArr.append(int(input()))

coinArr.sort(reverse=True)

result = 0
for i in coinArr:
    if K == 0:
        break
    result += K//i
    K %= i
print(result)