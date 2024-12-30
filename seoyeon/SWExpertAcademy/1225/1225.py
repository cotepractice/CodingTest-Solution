from collections import deque

def cycle(Q):
    global result
    cnt = 1
    while True:
        if cnt==6:
            return Q

        first = Q.popleft()
        first -= cnt
        if first <= 0:
            first = 0
            Q.append(first)
            result = 1
            return Q
        Q.append(first)

        cnt += 1

# import sys
# sys.stdin = open("input.txt", "r")

for i in range(1,11):
    k = int(input())
    Q_lst = list(map(int,input().split()))
    Q = deque(Q_lst)
    result = 0 
    while True:
        Q = cycle(Q)
        if result == 1:
            break
    print("#",k,sep="",end=" ")
    print(*Q)