def dfs(rx, ry, bx, by, cnt):
    global res
    if cnt == 11 or (bx, by) == (ox, oy):
        return
    if (rx, ry) == (ox, oy):
        res = min(res, cnt)
        return

    for dx, dy in delta:
        # 이동하려는 방향을 기준으로 누가 더 그 방향에 가깝게 있는지 확인 후 더 가깝게 있는 구슬부터 이동시킴
        if (rx * dx, ry * dy) > (bx * dx, by * dy):
            nrx, nry = move(rx, ry, dx, dy, bx, by)
            nbx, nby = move(bx, by, dx, dy, nrx, nry)

        else:
            nbx, nby = move(bx, by, dx, dy, rx, ry)
            nrx, nry = move(rx, ry, dx, dy, nbx, nby)

        # 위치가 바뀐게 없으면 continue
        if (nrx, nry) == (rx, ry) and (nbx, nby) == (bx, by):
            continue
        # 위치가 바뀐게 있으면 dfs 진행
        else:
            dfs(nrx, nry, nbx, nby, cnt + 1)


def move(x, y, dx, dy, cx, cy):
    while (1):
        x, y = x + dx, y + dy
        if board[x][y] == 'O':
            return (x, y)
        if board[x][y] == '#' or (x, y) == (cx, cy):
            x, y = x - dx, y - dy
            return (x, y)


N, M = map(int, input().split())
board = []

for i in range(N):
    lst = list(input())
    board.append(lst)
    for j in range(M):
        if lst[j] == 'R':
            lst[j] = '.'
            rx, ry = i, j
        elif lst[j] == 'B':
            lst[j] = '.'
            bx, by = i, j
        elif lst[j] == 'O':
            ox, oy = i, j

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 11
dfs(rx, ry, bx, by, 0)
res = -1 if res == 11 else res
print(res)