#정확성: 91.3

from collections import deque

dp = []
n = 0
m = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(maps,sx,sy,check):
    visited=[[False for _ in range(m)] for _ in range(n)]
    Q = deque()
    Q.append((sx,sy))
    visited[sx][sy] = True
    if check == 0:
        match = "L"
    else:
        match = "E"
    
    while Q:
        x,y = Q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False and maps[nx][ny] == "O": 
                    dp[nx][ny] = dp[x][y] + 1
                    visited[nx][ny] = True
                    Q.append((nx,ny))
                if visited[nx][ny]==False and maps[nx][ny] == match:
                    dp[nx][ny] = dp[x][y] + 1
                    visited[nx][ny] = True
                    return dp[nx][ny]
    
    return -1
    


def solution(maps):
    global n,m,dp
    answer,check = 0,0
    n = len(maps)
    m = len(maps[0])
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    s,e,l = [-1,-1], [-1,-1], [-1,-1]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                s = [i,j]
            if maps[i][j] == "L":
                l = [i,j]
            if maps[i][j] == "E":
                e = [i,j]
    
    #BFS 사용 => 레버 탐색
    answer = bfs(maps,s[0],s[1],check)
    if answer == -1:
        return answer
    check = 1
    #BFS 사용 => 출구 탐색
    answer = bfs(maps,l[0],l[1],check)
    
    return answer

#정확성 100/100
from collections import deque

dp = []
n = 0
m = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(maps,sx,sy,check):
    visited=[[False for _ in range(m)] for _ in range(n)]
    Q = deque()
    Q.append((sx,sy))
    visited[sx][sy] = True
    if check == 0:
        match = "L"
    else:
        match = "E"
    
    while Q:
        x,y = Q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False and maps[nx][ny] == match:
                    dp[nx][ny] = dp[x][y] + 1
                    visited[nx][ny] = True
                    return dp[nx][ny]
                
                if visited[nx][ny]==False and maps[nx][ny] != "X": 
                    dp[nx][ny] = dp[x][y] + 1
                    visited[nx][ny] = True
                    Q.append((nx,ny))

    return -1
    


def solution(maps):
    global n,m,dp
    answer,check = 0,0
    n = len(maps)
    m = len(maps[0])
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    s,e,l = [-1,-1], [-1,-1], [-1,-1]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                s = [i,j]
            if maps[i][j] == "L":
                l = [i,j]
            if maps[i][j] == "E":
                e = [i,j]
    
    #BFS 사용 => 레버 탐색
    answer = bfs(maps,s[0],s[1],check)
    if answer == -1:
        return -1
    check = 1
    #BFS 사용 => 출구 탐색
    answer = bfs(maps,l[0],l[1],check)
    
    return answer
