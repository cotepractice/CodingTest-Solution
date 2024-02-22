#백준 #21610 마법사 상어와 비바라기
#삼성 SW 역량 테스트 기출
from collections import deque

n, m = map(int, input().split())
buckets = [[0 for _ in range(n)] for _ in range(n)]
move = deque([])

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
cloudLst1 = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

#main
while move:
    #1. 모든 구름이 d 방향으로 s만큼 이동
    d,s = move.popleft()
    cloudMoved = []

    for k in range(len(cloudLst1)):
        x,y = cloudLst1[k]
        nx = x + s*dx[d-1]
        ny = y + s*dy[d-1]

        while True:
            if nx<0:
                nx += n
                
            elif nx>n-1: 
                nx -= n
                
            elif 0<=nx<n:
                    break
        while True:
            if ny<0:
                ny += n
            elif ny>n-1:
                ny -= n
            elif 0<=ny<n:
                break

        cloudMoved.append((nx,ny))


    #2. 각 구름에 비가 내리고 사라짐
    for k in range(len(cloudMoved)):
        x, y = cloudMoved[k]
        buckets[x][y] += 1

    #3. 대각선 개수 구해서 bucket에 추가
    for k in range(len(cloudMoved)):
        x, y = cloudMoved[k]
        cnt = 0
        for k in range(4):
            nx = x+rx[k]
            ny = y+ry[k]
            
            if 0<=nx<n and 0<=ny<n:
                if buckets[nx][ny] > 0:
                    cnt += 1
        buckets[x][y] += cnt

    #4. 물의 양 2 이상인 칸에 구름 생김 => 이때 물의 양이 2만큼 줄어듬
    cloudLst2 = []
    for i in range(n):
        for j in range(n):
            if buckets[i][j] >= 2:
                if (i,j) not in cloudMoved:
                    cloudLst2.append((i,j))
                    buckets[i][j] -= 2

    if (move == deque([])):
        sum = 0
        for i in range(n):
            for j in range(n):
                sum += buckets[i][j]
        print(sum)
        continue
    cloudLst1 = cloudLst2
