N, M = map(int, input().split())
INF = 1e6
dp = [INF] * (10001)
num = []
for _ in range(N):
    n = int(input())
    num.append(n)
    dp[n] = 1

for i in range(1, M+1):
    for j in num:
        if i-j >= 1 :
            dp[i] = min(dp[i-j]+1, dp[i])

dp[M] = dp[M] if dp[M]!=INF else -1 #M원을 만들 수 없는 경우에는 -1

print(dp[M])