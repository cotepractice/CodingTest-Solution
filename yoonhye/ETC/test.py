from collections import defaultdict
def solution(a, b):
    if a == info[b] or a == 1:
        return 1
    else:
        if(info.get(b)):
            return solution(a, info[b])
    return 0

N = int(input())
info = dict
for i in range(N-1):
    u, v = map(int, input().split())
    info[v] = u  #v의 부모 u
#print(info)
Q = int(input())
for i in range(Q):
    a, b, = map(int, input().split())
    print(solution(a,b), end=" ")