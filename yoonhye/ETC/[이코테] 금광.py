from collections import deque

T = int(input())
res_arr = []
for _ in range(T):
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    gold = []
    j = 0
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        gold.append(arr[j:j+m])
        dp[i][0] = arr[j]
        j += m

    queue = deque()
    for i in range(n):
        queue.append((i,0))    #첫 번째 열 index 삽입
    d = [(0,1), (1,1), (-1,1)]
    while(queue):
        x,y = queue.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            dp[nx][ny] = max(dp[x][y] + gold[nx][ny], dp[nx][ny])
            queue.append((nx,ny))

    res = 0
    for k in range(n):
        res = max(res, dp[k][-1])
    res_arr.append(res)

for r in res_arr:
    print(r)
