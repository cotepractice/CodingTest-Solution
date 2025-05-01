#백준 #10844 쉬운 계단 수
#14:19-

#1. 시간복잡도 O(N*(10*2*N)).1<=N<=100 -> 시간초과 발생
#구현

N = int(input())

dp = [0 for _ in range(N+1)]

#dp:길이가 1인 계단 수 = solv(1)
#길이가 2인 계단 수 = dp[1]+solv(2)
#길이가 3인 계단 수 = dp[2]+solv(3)
def solv(k,lst):
    #종결 조건
    if len(lst)==k:
        dp[k] += 1
        return
    
    last = lst[-1]
    tmp1,tmp2 = lst[:],lst[:]
    #인접한 모든 차이가 1
    if 0<=last+1<=9:
        tmp1.append(last+1)
        solv(N,tmp1)
    if 0<=last-1<=9:
        tmp2.append(last-1)
        solv(N,tmp2)

#i:길이가 N인 계단 수
for i in range(1,N+1):
    #j:1~9까지의 수. 0으로 시작하는 수는 계단 수가 아님
    for j in range(1,10):
        lst = [j]
        solv(i,lst)
print(dp[N])