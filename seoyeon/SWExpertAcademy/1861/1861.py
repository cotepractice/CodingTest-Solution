#SWExpert Academy
from collections import deque

def dfs(start_x,start_y):
    global N, matrix

    cnt = 0
    Q = deque()
    Q.append((start_x,start_y))
    while Q:
        x,y = Q.popleft()
        cnt += 1
        d_lst = [[1,0],[-1,0],[0,1],[0,-1]]
        for dx,dy in d_lst:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N:
                if matrix[nx][ny] == matrix[x][y]+1:
                    Q.append((nx,ny))
    return cnt

T = int(input())

for t in range(1,T+1):
    N = int(input())

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        matrix_lst = list(map(int,input().split()))
        matrix[i] = matrix_lst
    
    answer = [float("inf"), 0] #출발하는 방 번호, 이동 가능한 방의 개수

    for i in range(N):
        for j in range(N):
            cnt = dfs(i,j)
            if cnt==answer[1]:
                answer[0] = min(matrix[i][j], answer[0])
            elif cnt>answer[1]:
                answer[0] = matrix[i][j]
                answer[1]=cnt
            
    print("#",t,sep="",end=" ")
    print(answer[0],answer[1]) 