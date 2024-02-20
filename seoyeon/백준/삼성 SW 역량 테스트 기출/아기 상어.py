#백준 #16236 아기 상어
#삼성 SW 역량 테스트 기출
from collections import deque

n = int(input())
region = [[0 for _ in range(n)] for _ in range(n)]
pass_dp = [[False for _ in range(n)] for _ in range(n)]  #지나갈 수 있는지 여부
eat_dp = [[False for _ in range(n)] for _ in range(n)]  #먹을 수 있는지 여부

for i in range(n):
    region[i] = list(map(int, input().split()))

w = 2   #상어 초기 무게
x,y = -1,-1
t = 0   #소요 시간

for i in range(n):
    for j in range(n):
        if region[i][j] == 9: #같아도 지나갈 수는 있는데 먹는 것은 안 됨
            x=i
            y=j
        elif 0<=region[i][j]<=2:
            pass_dp[i][j] = True
        elif 0<=region[i][j]<2:
            eat_dp[i][j] = True

dx = [-1,0,0,1]
dy = [0,-1,1,0]

#bfs 사용 => 인접한 위치의 먹을 물고기 모두 찾기
def bfs(x,y,region):
    find = deque([])
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if (0<=nx<n and 0<=ny<n):
            if (1<=region[nx][ny]<=6 and region[nx][ny]<w): #자신의 크기보다 "작은" 물고기만 먹을 수 있음
                find.append((nx,ny))
    return find

#main
while True:
    #더이상 먹을 수 있는 물고기가 없는 경우
    find = bfs(x,y,region)
    if find == deque([]):
        break
    #먹을 물고기 위치를 갈 수 있는지(dp로) 확인
    else:
        t += 1
        fx,fy = find.popleft()  #물고기의 위치:fx,fy

print(t)