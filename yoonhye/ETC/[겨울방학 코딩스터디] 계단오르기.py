N = int(input())
dp = [1 for _ in range(45)] #dp[i] = i!(팩토리얼)
for i in range(2, N+1):
    dp[i] = i * dp[i-1]

cnt = 1 #2의 개수가 0개인 경우 총 1가지 (한 계단씩 오른 경우)
for i in range(1, (N//2)+1):
    j = N - 2*i #2의 개수가 i개인 경우 1의 개수
    total = N-i

    cnt += dp[total]//(dp[i]*dp[j])

print(cnt)




