#x가 3으로 나누어 떨어지면, 3으로 나눈다.
#x가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.

N = int(input())
dp = dict()
dp[1] = 0
for i in range(1, N):
    v = dp[i] + 1
    dp[i*3] = min(v, dp.get(i*3, N))
    dp[i*2] = min(v, dp.get(i*2, N))
    dp[i+1] = min(v, dp.get(i+1, N))

print(dp[N])

