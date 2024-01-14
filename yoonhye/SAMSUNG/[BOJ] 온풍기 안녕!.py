#성능 테스트 과정
#1. 집에 있는 모든 온풍기에서 바람이 한 번 나온다. (온풍기에서 바람이 나오는 방향에 따라 해당 방향으로 온도가 증가함)
#어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면, (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다.
#그 칸이 존재하지 않는다면, 바람은 이동하지 X. 온풍기에서 바람이 한 번 나왔을 때, 어떤 칸에 같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.
#일부 칸과 칸 사이에는 벽이 있어 온풍기 바람이 지나갈 수 없다.
#온풍기가 있는 칸도 다른 온풍기에 의해 온도가 상승할 수 있다.
#2. 온도가 조절된다.
#모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 (두 칸의 온도 차이)/4를 반내림한 만큼 온도가 조절된다. (모든 칸에 대해서 동시에 발생)
#인접한 두 칸 사이에 벽이 있는 경우에는 온도가 조절되지 않는다.
#3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
#4. 초콜릿을 하나 먹는다.
#5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
#구사과가 먹은 초콜릿의 개수를 출력. 만약, 먹는 초콜릿의 개수가 100을 넘어가면 101을 출력한다.
#1~4 => 오, 왼, 위, 아래
from collections import deque
def wind(x,y,d) :
    global R, C
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    delta = [[(-1,1),(0,1),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)]]
    sx, sy = x+direction[d][0], y+direction[d][1]
    visited = []
    if wall.get((x,y,sx,sy)) == None :
        board[sx][sy] += 5
    queue = deque([(sx, sy, 5)])
    while(queue):
        a, b, k = queue.popleft()
        if k==1:
            break
        for i in range(3):
            dx, dy = delta[d][i]
            nx, ny = a+dx, b+dy
            if nx<0 or ny<0 or nx>=R or ny>=C or (nx,ny) in visited:  #해당 위치에 도달할 수 있는지 먼저 확인
                continue
            success = False
            if i == 1:
                if wall.get((a, b, nx, ny)) == None:
                    success = True
            else:
                if wall.get((a, b, nx - direction[d][0], ny - direction[d][1])) == None:
                    if wall.get((nx-direction[d][0], ny-direction[d][1],nx,ny)) == None:
                        success = True

            if (success):
                visited.append((nx,ny))
                board[nx][ny] += k-1
                queue.append((nx,ny,k-1))
def temperature():
    global R, C
    new_board = [board[i][:] for i in range(R)]
    delta = [(0,1), (1,0)]  #오, 아래
    for i in range(R):
        for j in range(C):
            for dx, dy in delta:
                nx, ny = i+dx, j+dy
                if nx<0 or ny<0 or nx>=R or ny>=C or wall.get((i,j,nx,ny)) != None:
                    continue
                dt = abs(new_board[i][j]-new_board[nx][ny])//4
                if new_board[i][j] < new_board[nx][ny] :
                    board[nx][ny] -= dt
                    board[i][j] += dt
                else:
                    board[nx][ny] += dt
                    board[i][j] -= dt
def decrease_outside():
    global R, C
    for i in range(1,R-1):
        if board[i][0] >= 1:
            board[i][0] -= 1
        if board[i][-1] >= 1:
            board[i][-1] -= 1
    for j in range(C):
        if board[0][j] >= 1:
            board[0][j] -= 1
        if board[-1][j] >= 1:
            board[-1][j] -= 1

R, C, K = map(int, input().split())
board = []
heater = []
check = []
for i in range(R):
    board.append([int(x) for x in input().split()])
    for j in range(C):
        if 1<= board[i][j] <=4: #온풍기 정보 저장
            heater.append((i,j,board[i][j]-1))  #방향 : 0~3 -> 오, 왼, 위, 아래
            board[i][j] = 0
        elif board[i][j] == 5:
            check.append((i,j))
            board[i][j] = 0

W = int(input())    #벽의 개수
wall = dict()
for i in range(W):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if t == 0 :
        wall[(x,y,x-1,y)] = 1
        wall[(x-1,y,x,y)] = 1
    else :
        wall[(x,y,x,y+1)] = 1
        wall[(x,y+1,x,y)] = 1

chocolate = 0
for t in range(101):
    for x, y, d in heater:
        wind(x,y,d)
    temperature()
    decrease_outside()
    chocolate += 1
    success = True
    for a, b in check:
        if board[a][b] < K:
            success = False
            break
    if(success):
        break

print(chocolate)
