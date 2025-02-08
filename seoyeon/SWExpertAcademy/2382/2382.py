#SWExpert Academy #2382 미생물 격리

import sys
sys.stdin = open("input.txt", "r")

import copy

def up(x,y,num,d,cp_board):
    global visited 
    cp_board[x][y] = [0,0]
    x -= 1

    #방향 변경&미생물 수 변경
    if x==0 or x==N-1 or y==0 or y==N-1:
        d = 2 #방향 아래로 변경
        cp_board[x][y] = [num//2,d]
    else:
        cp_board[x][y] = [num,d]
    return cp_board
    
def down(x,y,num,d,cp_board):
    cp_board[x][y]=[0,0]
    x += 1

    #방향 변경&미생물 수 변경
    if x==0 or x==N-1 or y==0 or y==N-1:
        d = 1 #방향 위로 변경
        cp_board[x][y] = [num//2,d]
    else:
        cp_board[x][y] = [num,d]
    return cp_board

def left(x,y,num,d,cp_board):
    cp_board[x][y]=[0,0]
    y -= 1

    #방향 변경&미생물 수 변경
    if x==0 or x==N-1 or y==0 or y==N-1:
        d = 4 #방향 위로 변경
        cp_board[x][y] = [num//2,d]
    else:
        cp_board[x][y] = [num,d]
    return cp_board    

def right(x,y,num,d,cp_board):
    cp_board[x][y]=[0,0]
    y += 1

    #방향 변경&미생물 수 변경
    if x==0 or x==N-1 or y==0 or y==N-1:
        d = 3 #방향 위로 변경
        cp_board[x][y] = [num//2,d]
    else:
        cp_board[x][y] = [num,d]
    return cp_board    

def move():
    cp_board = copy.deepcopy(board)
    #print(cp_board)
    visited=[[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            num,dir = board[i][j] #미생물 수, 이동방향
            if x==-1:
                continue
            if dir==1:
                cp_board = up(i,j,num,dir,cp_board)
            elif dir==2:
                cp_board = down(i,j,num,dir,cp_board)
            elif dir==3:
                cp_board = left(i,j,num,dir,cp_board)
            elif dir==4:
                cp_board = right(i,j,num,dir,cp_board)
    return cp_board

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split())
    board = [[[0,0] for _ in range(N)] for _ in range(N)]

    for m in range(K):
        x,y,n,d = list(map(int,input().split()))
        board[x][y] = [n,d]
    
    for _ in range(M):
        board = move()
        #print(board)
        

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += board[i][j][0]
    print("#",t,sep="",end=" ")
    print(ans)