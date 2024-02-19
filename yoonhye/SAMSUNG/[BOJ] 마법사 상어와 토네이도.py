#격자 밖으로 나간 모래의 양 return

def move(x, y, d):
    global N, res
    v = board[x+d[0]][y+d[1]] #토네이도가 이동한 곳에 존재하는 모래의 양
    board[x+d[0]][y+d[1]] = 0
    ver, hor = [(1,0), (-1,0)], [(0,1), (0,-1)]
    if v == 0:
        return

    if d[0] == 0:    #왼쪽이나 오른쪽으로 이동
        move = ver
    else:   #위쪽이나 아래쪽으로 이동
        move = hor

    percentage = [v // 100, (v * 7) // 100, (v * 2) // 100, v // 10, (v * 5) // 100]    #one, seven, two, ten, five
    a = v - (2*sum(percentage)) + percentage[-1]
    for p in range(4):
        if p == 2:  #2%인 경우
            x -= d[0]
            y -= d[1]
            for dx, dy in move:
                nx, ny = x + (2*dx), y + (2*dy)
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                board[nx][ny] += percentage[p]
        else:
            for dx, dy in move:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                board[nx][ny] += percentage[p]

            if p==3:    #a로 이동한 경우
                if 0<=x<N and 0<=y<N:
                    board[x][y] += a
        x += d[0]
        y += d[1]
    if 0<=x<N and 0<=y<N:
        board[x][y] += percentage[-1]

def total():
    res = 0
    for arr in board:
        res += sum(arr)
    return res

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
init = total()
dir = [(0,-1), (1,0), (0,1), (-1,0)]    #좌, 하, 우, 상
d = 0
x, y = N//2, N//2
for i in range(1,N):
    if i == N-1:
        t = 3
    else:
        t = 2
    for j in range(t):
        for k in range(i):
            move(x,y, dir[d])
            x += dir[d][0]
            y += dir[d][1]

        d = (d + 1) % 4

answer = init - total()
print(answer)