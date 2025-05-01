#백준 #1463 1로 만들기

N = int(input())

dp = [float("inf") for _ in range(N+1)]

def solv(num,cnt):
    dp[num] = min(dp[num],cnt)

    if num<=1:
        return

    if num%3==0:
        solv(num//3,cnt+1)
    if num%2==0:
        solv(num//2,cnt+1)
    solv(num-1,cnt+1)

solv(N,0)
print(dp[1])