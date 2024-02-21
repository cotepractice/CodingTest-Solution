#백준 #21610 마법사 상어와 비바라기
#삼성 SW 역량 테스트 기출
from collections import deque

n, m = map(int, input().split())
buckets = [[0 for _ in range(n)] for _ in range(n)]
clouds = [[False for _ in range(n)] for _ in range(n)]
move = deque([])

print("cloud",clouds)

for i in range(n):
    buckets[i] = list(map(int, input().split()))

for k in range(m):
    d,s = map(int, input().split())
    move.append((d,s))

#방향별 좌표 이동
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

#대각선 체크
rx = [-1,-1,1,1]
ry = [-1,1,-1,1]

#(n-2,0),(n-2,1),(n-1,0),(n-1,1),에 구름 존재
cloudPos = deque([(n-2,0),(n-2,1),(n-1,0),(n-1,1)])

#main
#1. 모든 구름이 d 방향으로 s만큼 이동
d,s = move.popleft()
for k in range(len(cloudPos)):
    x,y = cloudPos.popleft()
    nx = x + s*dx[d-1]
    ny = y + s*dy[d-1]

    if nx<0:
        while True:
            nx += n
            if 0<=nx<n:
                break
    elif nx>n-1:
        while True: 
            nx -= n
            if 0<=nx<n:
                break
    elif ny<0:
        while True:
            ny += n
            if 0<=ny<n:
                break
    elif ny>n-1:
        while True:
            y -= n
            if 0<=y<n:
                break
    
    cloudPos.append((nx,ny))

#2. 각 구름에 비가 내리고 사라짐
while cloudPos:
    x, y = cloudPos.popleft()
    cloudPos.append((x,y))
    buckets[x][y] += 1

#3. 

print("clouds",clouds)
print("buckets",buckets)