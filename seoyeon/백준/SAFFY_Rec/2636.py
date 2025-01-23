#백준 #2636 치즈
#BFS

#0을 -1로 만드는 bfs 함수
def first_func(t):

    global matrix,N,M
    
    Q = deque()

    #겉에 있는 0을 모두 -1로 변경
    if t==0:
        for j in range(M):
            if matrix[0][j]==0:
                matrix[0][j] = -1
                Q.append([0,j])
            elif matrix[N-1][j]==0:
                matrix[N-1][j] = -1
                Q.append([N-1,j])
        
        for i in range(N):
            if matrix[i][0]==0:
                matrix[i][0] = -1
                Q.append([i,0])
            elif matrix[i][M-1]==0:
                matrix[i][M-1] = -1
                Q.append([i,M-1])
    else:
        for i in range(N):
            for j in range(M):
                if matrix[i][j]==0:
                    matrix[i][j] = -1
                    Q.append([i,j])

    #nx,ny로 상하좌우에 -1과 닿아있는 0이 있으면 모두 -1로 변경
    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    while Q:
        x,y = Q.popleft()
        for dx,dy in d_lst:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==0:
                matrix[nx][ny] = -1
                Q.append([nx,ny])

#1을 0으로 만드는 bfs 함수
def second_func():

    Q = deque()
    cnt = 0

    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==-1:
                for dx,dy in d_lst:
                    nx = i+dx
                    ny = j+dy
                    if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==1:
                        matrix[nx][ny]=0
                        cnt += 1
    return cnt



from collections import deque

N, M = map(int,input().split())
ans = [0,0] #ans[0]:치즈가 모두 녹는데 걸리는 시간,ans[1]:모두 녹기 한 시간 전 남아있는 치즈 조각 개수 

matrix = [[-1 for _ in range(M)] for _ in range(N)] 

for i in range(N):
    lst = list(map(int,input().split()))
    matrix[i]=lst

#처음
while True:
    first_func(ans[0])
    #print("1",matrix)
    cheese = second_func()
    #print("2",cheese)
    if cheese>0:
        ans[0] += 1
        ans[1] = cheese
    else:
        break

print(*ans,sep="\n")