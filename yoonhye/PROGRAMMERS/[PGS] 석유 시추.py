from collections import deque

def bfs(arr, i, j, num):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = len(arr[0]), len(arr)  # 열, 행
    queue = deque([(i, j)])
    count = 0
    while (queue):
        x, y = queue.popleft()
        if arr[x][y] > 1:
            continue
        arr[x][y] = num
        count += 1
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))

    return count


def solution(land):
    answer = 0
    m, n = len(land[0]), len(land)  # 열, 행
    num = 2
    oil = dict()
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                oil[num] = bfs(land, i, j, num)
                num += 1

    columns = [0 for _ in range(m)]
    for i in range(m):
        visited = set()
        for j in range(n):
            if land[j][i] > 1 and land[j][i] not in visited:
                visited.add(land[j][i])
                columns[i] += oil[land[j][i]]

    return max(columns)
