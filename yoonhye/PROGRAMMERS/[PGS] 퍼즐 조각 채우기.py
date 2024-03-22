from collections import deque
from collections import defaultdict

def setting(arr):
    l = len(arr)

    queue = deque()
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 좌,우,하,상

    cnt = 1
    for i in range(l):
        for j in range(l):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = cnt
                queue.append((i, j))

                while (queue):
                    x, y = queue.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= l or ny >= l:
                            continue
                        if arr[nx][ny] == 1:
                            arr[nx][ny] = cnt
                            queue.append((nx, ny))

def find(arr, n, board_type):
    l = len(arr)
    visited = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 좌,우,하,상

    if board_type == "game":
        blanks = defaultdict(list)
    else:
        blanks = defaultdict(dict)

    for i in range(l):
        for j in range(l):
            if visited[i][j] or arr[i][j] == n:
                continue
            else:
                visited[i][j] = 1
                queue.append((i, j, 0, 0))
                blank = [(0, 0)]
                while (queue):
                    x, y, a, b = queue.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= l or ny >= l:
                            continue
                        if arr[nx][ny] != n and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            queue.append((nx, ny, a + dx, b + dy))
                            blank.append((a + dx, b + dy))
                if board_type == "game":
                    blanks[len(blank)].append(blank)
                else:
                    blanks[len(blank)][arr[i][j]] = blank

    return blanks

def rotation(arr):
    l = len(arr)
    new_arr = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        k = l - 1
        for j in range(l):
            new_arr[i][j] = arr[k][i]
            k -= 1

    return new_arr


def solution(game_board, table):
    answer = 0
    blanks = find(game_board, 1, "game")
    setting(table)

    blocks = []
    for i in range(4):
        blocks.append(find(table, 0, "table"))
        table = rotation(table)

    res = dict()
    for length, blank in blanks.items():
        for b in blank:
            success = False
            for i in range(4):
                for key, value in blocks[i][length].items():

                    if value == b and res.get(key) == None:
                        success = True
                        res[key] = len(b)
                        break
                if success:
                    break

    for key, value in res.items():
        answer += value

    return answer