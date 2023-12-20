#전투력이 높은 병사가 앞쪽. 특정한 위치에 있는 병사를 열외시키는 방법으로 배치.
#남아있는 병사의 수가 최대가 되도록.

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]: #내림차순 만족
            dp[i] = max(dp[i], dp[j]+1)

res = N-max(dp)
print(res)



