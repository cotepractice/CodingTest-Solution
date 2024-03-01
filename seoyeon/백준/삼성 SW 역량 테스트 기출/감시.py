#백준 #15683 감시
#삼성 SW 역량 테스트 기출

N,M = map(int, input().split())
Rooms = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    Rooms[i] = list(map(int, input().split()))

def one(i,j):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    maxIdx = 0
    maxCnt = 0
    for k in range(4):
        cnt = 0
        n = 1
        x = i+dx[k]
        y = j+dy[k]
        while 0<=x<N and 0<=y<M and Rooms[x][y]!=6:
            if Rooms[x][y]==0:  #빈 칸만 카운트. CCTV이거나 이미 감시한 곳은 카운트 X
                cnt += 1
            n += 1
            x = i+dx[k]*n
            y = j+dy[k]*n

        if cnt > maxCnt:
            maxCnt = cnt
            maxIdx = k
    
    x = i+dx[maxIdx]
    y = j+dy[maxIdx]
    n = 1
    while 0<=x<N and 0<=y<M and Rooms[x][y]!=6:
        Rooms[x][y] = 7 #cctv 감시 구역
        n += 1
        x = i+dx[maxIdx]*n
        y = j+dy[maxIdx]*n
    return Rooms

def two(i,j):
    directions = [[(0,-1),(0,1)],[(-1,0),(1,0)]]
    cnt = 0

    maxIdx = 0
    maxCnt = 0
    for direction in directions:
        for k in range(2):
            x = i+direction[k][0]
            y = j+direction[k][1]
            n = 1
            
            while 0<=x<N and 0<=y<M and Rooms[x][y]!=6:
                if Rooms[x][y]==0:
                    cnt+=1
                n += 1
                x = i+direction[k][0]*n
                y = j+direction[k][1]*n

        if cnt > maxCnt:
            maxCnt = cnt
            maxIdx = direction
        cnt = 0
    
    for k in range(2):
        x = i+maxIdx[k][0]
        y = j+maxIdx[k][1]

        while 0<=x<N and 0<=y<M and Rooms[x][y]!=6:
            if Rooms[x][y]==0:
                Rooms[x][y] = 7
            x += maxIdx[k][0]
            y += maxIdx[k][1]
    return Rooms


for i in range(N):
    for j in range(M):
        if Rooms[i][j] == 1:
            one(i,j)
        elif Rooms[i][j] == 2:
            two(i,j)
        # elif Rooms[i][j] == 3:
        #     three(i,j)
        # elif Rooms[i][j] == 4:
        #     four(i,j)
        # elif Rooms[i][j] == 5:
        #     five(i,j)

print(*Rooms)
cnt = 0
for i in range(N):
    for j in range(M):
        if Rooms[i][j] == 0:
            cnt += 1

print(cnt)