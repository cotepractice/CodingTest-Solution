def move_down(x, y, d):
    global L
    if x + 2 >= L or board[x + 2][y] or board[x + 1][y - 1] or board[x + 1][y + 1]:
        return move_left(x, y, d)
    return (x + 1, y, d)


def move_left(x, y, d):
    global L
    if y - 2 < 0 or board[x][y - 2] or board[x - 1][y - 1] or board[x + 1][y - 1]:
        return move_right(x, y, d)
    if x + 2 >= L or board[x + 2][y - 1] or board[x + 1][y - 2] or board[x + 1][y]:
        return move_right(x, y, d)
    d -= 1
    if d < 0:
        d = d + 4
    return (x + 1, y - 1, d)


def move_right(x, y, d):
    global L, C
    if y + 2 >= C or board[x][y + 2] or board[x - 1][y + 1] or board[x + 1][y + 1]:
        return False
    if x + 2 >= L or board[x + 2][y + 1] or board[x + 1][y + 2] or board[x + 1][y]:
        return False

    d = (d + 1) % 4
    return (x + 1, y + 1, d)


def get_score(i):
    global L, C
    stack = [i]
    visited = set({i})
    max_score = 0
    while (stack):
        n = stack.pop()
        x, y, d = robot[n]
        max_score = max(max_score, x + 1)
        ex, ey = x + delta[d][0], y + delta[d][1]
        for dx, dy in delta:
            nx, ny = ex + dx, ey + dy
            if nx < 0 or ny < 0 or nx >= L or ny >= C or board[nx][ny] == 0:
                continue
            if board[nx][ny] != n and board[nx][ny] not in visited:
                stack.append(board[nx][ny])
                visited.add(board[nx][ny])

    return max_score - 2


R, C, K = map(int, input().split())
L = R + 3
board = [[0 for _ in range(C)] for _ in range(L)]


#상우하좌 => 0~3
req = []
robot = dict()
score = 0
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(K):
    c, d = map(int, input().split())
    req.append((c-1, d))

for i in range(1, K + 1):
    x, y, d = 1, req[i - 1][0], req[i - 1][1]
    while (1):
        result = move_down(x, y, d)
        if result == False:
            break
        x, y, d = result

    if x <= 3:
        board = [[0 for _ in range(C)] for _ in range(L)]
        continue
    board[x][y] = i
    for j in range(4):
        board[x + delta[j][0]][y + delta[j][1]] = i

    robot[i] = (x, y, d)
    score += get_score(i)
print(score)