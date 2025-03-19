from collections import deque
    

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    dp = [[float("inf") for _ in range(m)] for _ in range(n)]
    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    
    Q = deque()
    Q.append([0,0,1])
    dp[0][0]=1
    
    while Q:
        current_x,current_y,cnt = Q.popleft()
        
        for dx,dy in d_lst:
            next_x,next_y = current_x+dx,current_y+dy
            if 0<=next_x<n and 0<=next_y<m and maps[next_x][next_y]==1:
                if cnt+1 < dp[next_x][next_y]:
                    dp[next_x][next_y]=cnt+1
                    Q.append([next_x,next_y,cnt+1])
    
    if dp[n-1][m-1]==float("inf"):
        answer = -1
    else:
        answer = dp[n-1][m-1]
    
    return answer