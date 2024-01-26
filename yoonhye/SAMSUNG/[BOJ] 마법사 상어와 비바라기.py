#바구니에 저장할 수 있는 물의 양에는 제한이 없다.
#(1,1) ~ (N,N)
#1번 열 왼쪽에 N번 열, 1번 행 위쪽에 N번 행 존재.
#(N,1), (N,2), (N-1,1), (N-1,2)에 비구름이 생김. 구름은 칸 전체를 차지한다.
#왼쪽부터 시계방향으로 총 8개의 방향. (1~8)
#1. 모든 구름이 d 방향으로 s칸 이동
#2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
#3. 구름이 모두 사라짐
#4. 2에서 물이 증가한 칸에 물복사버그 마법 시전.
#   대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 마법 시전한 칸에 있는 바구니의 물 양이 증가.
#   이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 X!!
#5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦.
#   이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
#M번 이동 후 바구니에 들어있는 물의 양의 합
from collections import deque
def cloud_move(d, s):   #구름 이동 함수
    global N
    new_cloud = []
    dx, dy = dir[d]
    for x, y in cloud:
        for _ in range(s):
            x, y = x+dx, y+dy
            if x == -1:
               x = N-1
            elif x == N:
                x = 0
            if y == -1:
                y = N-1
            elif y == N:
                y = 0
        new_cloud.append((x,y))
    return new_cloud

def water_copy():
    global N
    delta = [(-1,-1), (-1,1), (1,-1), (1,1)]    #대각선
    for x, y in cloud:
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if board[nx][ny]:   #물이 있으면
                board[x][y] += 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move_info = deque()
dir = [(0,0), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)] #1~8 => 왼쪽부터 시계방향
for _ in range(M):
    d, s = map(int, input().split())
    move_info.append((d,s))
cloud = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]

for _ in range(M):
    d, s = move_info.popleft()
    cloud = cloud_move(d,s)
    for x, y in cloud:
        board[x][y] += 1
    del_cloud = dict().fromkeys(cloud,0)
    water_copy()
    cloud = []

    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and del_cloud.get((i,j)) == None:
                cloud.append((i,j))
                board[i][j] -= 2
res = 0
for i in range(N):
    res += sum(board[i])
print(res)