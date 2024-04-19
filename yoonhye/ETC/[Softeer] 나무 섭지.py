# 남우가 유령보다 더 빨리 출구에 도달할 수 있으면 탈출 가능

from collections import deque


def bfs(x, y, type=''):
    global n, m
    queue = deque([(x, y, 1)])
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1

    while (queue):
        x, y, cnt = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == type:
                continue
            if board[nx][ny] == 'D':
                return cnt
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    return -1


def distance(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))


n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
exit_x, exit_y = 0, 0
ghosts = []
nx, ny = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            exit_x, exit_y = i, j
        elif board[i][j] == 'G':
            ghosts.append((i, j))
        elif board[i][j] == 'N':
            nx, ny = i, j

if len(ghosts):
    gd_min, rgx, rgy = 2000, -1, -1
    for gx, gy in ghosts:
        d = distance(gx, gy, exit_x, exit_y)
        if d < gd_min:
            gd_min = d
            rgx, rgy = gx, gy

    gres = bfs(rgx, rgy)
else:
    gres = 1000000

nres = bfs(nx, ny, '#')

if nres < gres and nres != -1:
    print("Yes")
else:
    print("No")