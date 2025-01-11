#백준 #2839 설탕 배달

import sys
sys.setrecursionlimit(100000)

N = int(input())

def sol(cur_N,depth):
    global N,ans
    if cur_N > N:
        return
    if cur_N == N:
        ans = min(ans,depth)
        return N
    
    sol(cur_N+3,depth+1)
    sol(cur_N+5,depth+1)


ans = float("inf")
sol(0,0)
if ans==float("inf"):
    print(-1)
else:
    print(ans)