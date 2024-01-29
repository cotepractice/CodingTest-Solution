#모든 칸에는 블록이 하나씩 들어 있음. 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수. 검은색은 -1, 무지개는 0
#인접한 칸 => abs(r1-r2) + abs(c1-c2) == 1  => 상하좌우로 거리 1이면 인접
#그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
#검은색은 포함하면 안 되고, 무지개는 얼마나 있든 상관X.
#그룹에 속한 블록 수는 2이상, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
#블록 그룹의 기준 블록 : 일반 블록 중 행의 번호가 가장 작은 블록. (같으면 열이 가장 작은 블록)
#블록 그룹이 존재하는 동안 계속 반복.
#1. 크기가 가장 큰 블록 그룹을 찾는다. 크기가 같으면 포함된 무지개 블록 수가 가장 많은 블록, 기준 블록의 행이 큰 거, 열이 큰 거
#2. 1에서 찾은 블록 그룹의 모든 블록을 제거. B^2 점 획득. ( B = 블록 수)
#3. 격자에 중력이 작용(검은색 제외 모두 행의 번호가 큰 칸으로 이동. 이동은 다른 블록 or 격자의 경계를 만나기 전까지 계속됨)
#4. 격자 90도 반시계 방향으로 회전
#5. 다시 격자에 중력 작용
#최종적으로 획득한 점수의 합 출력
from collections import deque
def bfs():
    global N, res
    visited = [[0 for _ in range(N)] for _ in range(N)]
    delta = [(-1,0), (0,-1), (0,1), (1,0)]
    queue = deque()
    rainbow_num, row, column, group = 0, 0, 0, []
    for i in range(N):
        for j in range(N):
            if board[i][j]>0 and visited[i][j] == 0:  #일반 블록이고, 한 번도 방문한 적 없으면
                queue.append((i,j))
                n = board[i][j]
                nrainbow_num, nrow, ncolumn, ngroup = 0, i, j, []
                rainbow = []
                while(queue):
                    x, y = queue.popleft()
                    for dx, dy in delta:
                        nx, ny = x+dx, y+dy
                        if nx<0 or ny<0 or nx>=N or ny>=N or board[nx][ny] < 0:
                            continue
                        if visited[nx][ny] == 0:
                            if board[nx][ny] == n or board[nx][ny] == 0:
                                queue.append((nx, ny))
                                visited[nx][ny] = 1
                                ngroup.append((nx, ny))
                            if board[nx][ny] == 0:    #무지개이면
                                nrainbow_num += 1
                                rainbow.append((nx,ny))

                if len(group)<len(ngroup):
                    rainbow_num, row, column, group = nrainbow_num, nrow, ncolumn, ngroup
                elif len(group) == len(ngroup):
                    if rainbow_num < nrainbow_num or ((rainbow_num == nrainbow_num) and (row, column) < (nrow,ncolumn)):
                        rainbow_num, row, column, group = nrainbow_num, nrow, ncolumn, ngroup

                for a, b in rainbow:    #무지개 방문 여부 초기화
                    visited[a][b] = 0
    if len(group) <= 1:
        return False
    res += (len(group) ** 2)
    for i, j in group:
        board[i][j] = -2
    return True

def gravity_and_rotate():
    global N
    new_board = []
    for j in range(N - 1, -1, -1):
        new_col = [-2 for _ in range(N)]
        for i in range(N - 1, -1, -1):
            r = i
            if board[i][j] >= 0:
                while (0 <= r < N - 1 and new_col[r + 1] == -2):
                    r += 1
            new_col[r] = board[i][j]

        new_board.append(new_col)

    return new_board
def gravity():
    global N
    for j in range(N-1, -1, -1):
        new_col = [-2 for _ in range(N)]
        for i in range(N - 1, -1, -1):
            r = i
            if board[i][j] >= 0:
                while (0<=r<N-1 and new_col[r+1] == -2):
                    r += 1
            new_col[r] = board[i][j]

        for k in range(N):
            board[k][j] = new_col[k]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0
while(bfs()):
    board = gravity_and_rotate()
    gravity()
print(res)