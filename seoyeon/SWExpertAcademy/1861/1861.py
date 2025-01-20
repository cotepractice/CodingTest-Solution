#SWExpert Academy

def dfs(x,y,start,n):
    global rooms_n,max_n,N,matrix

    if n>=max_n:
        rooms_n=min(rooms_n,start)
        max_n=n
        
    m_lst = [[1,0],[-1,0],[0,1],[0,-1]]
    for dx,dy in m_lst:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<N:
            if matrix[nx][ny]==matrix[x][y]+1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny,start,n+1)
                visited[nx][ny]=False




T = int(input())

for t in range(1,T+1):
    N = int(input())

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        matrix_lst = list(map(int,input().split()))
        matrix[i] = matrix_lst
    
    rooms_n=float("inf") #출발하는방번호
    max_n=0 #이동가능한방개수

    visited=[[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            visited[i][j]=True
            dfs(i,j,matrix[i][j],1)
            visited[i][j]=False

    print("#",t,sep="",end=" ")
    print(rooms_n,max_n)