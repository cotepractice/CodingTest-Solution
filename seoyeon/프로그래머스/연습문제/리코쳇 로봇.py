from collections import deque

dp = [[]]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solve(start,end,board):
    global dp
    sx,sy = start[0],start[1]
    Q = deque()
    Q.append([sx,sy])

    while Q:
        x,y = Q.popleft()

        #종결조건
        if board[x][y]=="G":
            return dp[x][y]
        #방향선택
        for d in range(4):
            nx = x
            ny = y
            
            while True:
                nx += dx[d]
                ny += dy[d]
                
                #nx,ny를 마지막에 도착하는 좌표로 설정
                if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]) or board[nx][ny]=="D":
                    nx -= dx[d]
                    ny -= dy[d]
                    break
                    
            #마지막 위치(종료되는 위치)에만 dp 값 생성
            if not dp[nx][ny]:
                dp[nx][ny] = dp[x][y] + 1
                Q.append([nx,ny])
        
    return -1
    

def solution(board):
    answer = 0
    global dp
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    start = [-1,-1]
    end = [-1,-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start = [i,j]
                dp[i][j] = 1
            if board[i][j] == "G":
                end = [i,j]
    
    answer = solve(start,end,board)
    if answer > 0 :
        answer -= 1
                
    return answer