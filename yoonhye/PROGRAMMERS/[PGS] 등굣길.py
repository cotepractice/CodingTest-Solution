# (1,1)부터 시작.
# 오른쪽과 아래족으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지 return
# 좌표의 행열을 바꿔서 생각해야함.
# dp[i][j] = dp[i][j-1] + dp[i-1][j]

from collections import deque


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]  # n행 m열
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for y, x in puddles:
        board[x - 1][y - 1] = 1  # 물에 잠긴 지역

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                if 0 <= i - 1 < n:
                    dp[i][j] += dp[i - 1][j]
                if 0 <= j - 1 < m:
                    dp[i][j] += dp[i][j - 1]
    print(dp)
    return dp[n - 1][m - 1] % 1000000007