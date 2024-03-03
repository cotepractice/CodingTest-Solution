# (1,1)부터 시작.
# 오른쪽과 아래족으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지 return
# 좌표의 행열을 바꿔서 생각해야함.
from collections import deque


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]  # n행 m열
    dp = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (1, 0)]  # 오른쪽, 아래쪽
    for y, x in puddles:
        board[x - 1][y - 1] = 1  # 물에 잠긴 지역

    queue = deque([(0, 0)])

    dp[0][0] = 1

    while (queue):
        x, y = queue.popleft()
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0:
                dp[nx][ny] += dp[x][y]
                queue.append((nx, ny))
    print(dp)
    return dp[n - 1][m - 1] % 1000000007