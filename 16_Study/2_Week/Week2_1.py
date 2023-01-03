import sys
K, N = map(int, sys.stdin.readline().split())

lanArr = []
for i in range(K):
    lanArr.append(int(input()))

start = 1
end = max(lanArr)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt = lanArr[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid -1
print(end)