#백준 #16928 뱀과 사다리 게임

#Greedy. 틀렸습니다
from collections import defaultdict

N,M = map(int,input().split())
ladder = defaultdict() #ladder[x]=y. x<y
snake = defaultdict() #snake[u]=v. u>v

for i in range(N):
    x,y = map(int,input().split())
    ladder[x]=y
for i in range(M):
    u,v = map(int,input().split())
    snake[u]=v


#ladder 타야함
current = 1
dice = [i for i in range(1,7)]

cnt = 0
while True:
    cnt += 1
    next = current #현재 최종 위치
    max_next = current
    for i in dice:
        next = current+i
        if next in snake:
            next = snake[next]
        if next in ladder:
            next = ladder[next]
        max_next = max(max_next,next)
    if max_next>=100:
        break
    current = max_next

print(cnt)