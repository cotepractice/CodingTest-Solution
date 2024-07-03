# [PCCP 기출문제] 2번

#1. BFS 사용 => 정확성:60.0, 효율성:0.0, 총 60.0/100.0
from collections import deque

def bfs(x,y,cnt,visited,land):
    #print("x,y",x,y)
    global n,m
    Q = deque()
    Q.append((x,y))

    visited[x][y] = True
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while Q:
        mx,my = Q.popleft()
        cnt += 1
        for k in range(4):
            nx = mx+dx[k]
            ny = my+dy[k]
        
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False and land[nx][ny]==1:
                    #print("nxny",nx,ny)
                    Q.append((nx,ny))
                    visited[nx][ny] = True
                    #Q.append((nx,ny))
    return cnt            
    
    
def solution(land):
    #land[n][m]
    global n,m
    n = len(land)
    m = len(land[0])
    #visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    
    oil_amount = [0 for _ in range(m)]
    for i in range(m):
        visited = [[False for _ in range(m+1)] for _ in range(n+1)]
        for j in range(n):
            if land[j][i] == 1 and visited[j][i] == False:
                amount = bfs(j,i,0,visited,land)
                #print("amount",amount)
                oil_amount[i] += amount
            
    #print(oil_amount)
    answer = max(oil_amount)
    return answer

global n
global m 

#2. BFS 사용 => 정확성 60.0, 효율성 26.7, 합계 86.7/100
from collections import deque

def bfs(x,y,cnt,visited,land,comparison,compare):
    global n,m
    Q = deque()
    Q.append((x,y))
    lst = []


    visited[x][y] = True
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while Q:
        mx,my = Q.popleft()
        lst.append((mx,my))
        cnt += 1
        for k in range(4):
            nx = mx+dx[k]
            ny = my+dy[k]
        
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False and land[nx][ny]==1:
                    Q.append((nx,ny))
                    visited[nx][ny] = True
    #print("lst",lst)
    for k in range(len(lst)):
        
        land[lst[k][0]][lst[k][1]] = cnt
        compare[lst[k][0]][lst[k][1]] = comparison
            
    return cnt            
    
    
def solution(land):

    global n,m
    n = len(land)
    m = len(land[0])
    comparison = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    compare = [[-1 for _ in range(m)] for _ in range(n)]
    
    #석유 존재하는 모든 좌표에 석유양 표시 land[x][y]=AMOUNT
    for i in range(m):
        for j in range(n):
            if land[j][i] == 1 and visited[j][i] == False:
                bfs(j,i,0,visited,land,comparison,compare)
                comparison += 1
    
    oil_amount = [0 for _ in range(m)]
    #계산
    for i in range(m):
        amount = 0 
        already = []
        for j in range(n):
            check = 0
            #석유 없는 공간이면 패쓰
            if compare[j][i] == -1:
                continue
            #석유 있으면 이미 계산한 것과 겹치는지 확인
            for k in range(len(already)):
                if compare[j][i] == already[k]:
                    check = 1
            if check == 0:
                #겹치지 않을 때 
                already.append(compare[j][i])
                amount += land[j][i]
        oil_amount[i] = amount
    
    answer = max(oil_amount)

    return answer

global n
global m 
global comparison

#3. 정확성 60, 효율성 40, 합계 100
#덩어리 분리 list가 아닌 set 사용해 중복 방지 

from collections import deque

def bfs(x,y,cnt,visited,land,comparison):
    global n,m
    Q = deque()
    Q.append((x,y))
    column_lst = []   

    visited[x][y] = True
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while Q:
        mx,my = Q.popleft()
        column_lst.append(my)
        cnt += 1
        for k in range(4):
            nx = mx+dx[k]
            ny = my+dy[k]
        
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and land[nx][ny]==1:
                    Q.append((nx,ny))
                    visited[nx][ny] = True
    
    column_set = set(column_lst)        
    return cnt, column_set    #해당 덩어리의 크기와 덩어리가 존재하는 columns       
    
    
def solution(land):

    global n,m
    n = len(land)
    m = len(land[0])
    comparison = 1  #땅 비교. 1부터 점점 증가
    visited = [[0 for _ in range(m)] for _ in range(n)]
    oil_lst = []
    oil_amount = [0 for _ in range(m)]
    
    #석유 존재하는 모든 좌표에 석유양 표시 land[x][y]=AMOUNT
    for i in range(m):
        for j in range(n):
            if land[j][i] == 1 and visited[j][i] == 0:
                size,columns = bfs(j,i,0,visited,land,comparison)
                oil_lst.append([size, columns])
                comparison += 1
    
    for k in range(len(oil_lst)):
        for l in oil_lst[k][1]:
            oil_amount[l] += oil_lst[k][0]

    answer = max(oil_amount)

    return answer

global n
global m 
global comparison