#SWExpertAcademy #1868 파핑파핑 지뢰찾기
from collections import deque

#주변의 * 개수 카운트
def check(x,y):

    d_lst = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    cnt = 0

    for dx,dy in d_lst:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny]=="*":
                cnt += 1
    board[x][y]=cnt

#board[x][y]==0인 경우 주변 숫자 모두 *로 변경
def count_check(x,y):
    Q=deque()
    Q.append([x,y])
    visited[x][y] = True

    d_lst = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    while Q:
        i,j = Q.popleft()
        for dx,dy in d_lst:
            nx = i+dx
            ny = j+dy
            if 0<=nx<N and 0<=ny<N:
                #board[nx][ny]가 0인 경우, Q에 넣고 계속 진행
                if board[nx][ny]==0 and not visited[nx][ny]:
                    board[nx][ny]="*"
                    visited[nx][ny]=True
                    Q.append([nx,ny])
                #board[nx][ny]가 0이 아닌 숫자인 경우는 *로 변경. 다시 방문하지 않기 위해
                elif board[nx][ny]!="*":
                    board[nx][ny] = "*"


T = int(input())

for t in range(1,T+1):
    N = int(input())
    board = [[] for _ in range(N)]
    visited=[[False for _ in range(N)] for _ in range(N)]

    for n in range(N):
        lst = list(input())
        board[n] = lst
    
    ans = 0
    d_lst = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    #board에 주변의 * 개수 넣기
    for i in range(N):
        for j in range(N):
            if board[i][j]==".":
                check(i,j)

    #1.board[i][j]==0 먼저 클릭
    #더 넓게 탐색하기 위해
    #board[i][j]==0인 경우는 아직 해당 위치까지 진행하지 못한 것이므로 ans+1 후 진행
    for i in range(N):
        for j in range(N):
            if board[i][j]==0 and not visited[i][j]:
                ans += 1
                count_check(i,j)

    #2.아직 클릭되지 않은 "." 클릭
    for i in range(N):
        for j in range(N):
            if board[i][j]!="*" and not visited[i][j]:
                ans += 1

    print("#",t,sep="",end=" ")
    print(ans)