#맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로
#아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

dp = [[] for _ in range(n)] #dp[i][j] =>(i,j)가 선택됐을 때, 이때가지 선택된 수들의 최댓값. i층 j번까지의 최댓값.
                            # board[i][j] + max(dp[i-1][j], dp[i-1][j-1)]
for i in range(n):
    dp[i] = [0 for _ in range(i+1)]

dp[0][0] = board[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][0] + board[i][j]
        elif j == i :
            dp[i][j] = dp[i-1][j-1] + board[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + board[i][j]

print(max(dp[n-1]))
