#x가 3으로 나누어 떨어지면, 3으로 나눈다.
#x가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.

N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[N])

