# 처음 상어의 방향은 (0,0)에 있던 물고기의 방향과 같다.
# 물고기는 번호가 작은 물고기부터 순서대로 이동. 상어가 있거나 공간의 경계를 넘는 칸으로는 이동할 수 없다.
# 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전. 그래도 없으면 이동 X
# 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동.
# 물고기의 이동이 모두 끝나면 상어가 이동. 상어는 방향에 있는 칸으로 한 번에 여러 개 칸 이동 가능.
# 상어가 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않음. 물고기가 없는 칸으로는 이동 불가.
# 상어가 이동할 수 있는 칸이 없으면 공간을 벗어나 집으로 감.
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값.

def fishes_move(sx, sy, sd, arr, n, f_arr):
    new_board = [arr[i][:] for i in range(4)]
    fishes = f_arr[:]
    for i in range(1,17):
        if fishes[i] == 0:
            continue
        fx, fy, fd = fishes[i]
        for _ in range(8):
            nx, ny = fx + d[fd][0], fy + d[fd][1]
            if nx<0 or ny<0 or nx>=4 or ny>=4 or (nx,ny) == (sx,sy):
                fd = (fd+1)%8
                continue
            if new_board[nx][ny] == 0:
                new_board[nx][ny] = new_board[fx][fy]
                new_board[fx][fy] = 0
                fishes[i] = (nx, ny, fd)

            else:
                a, b = new_board[fx][fy], new_board[nx][ny]
                new_board[fx][fy], new_board[nx][ny] = b, a
                fishes[a], fishes[b] = (nx, ny, fd), (fx, fy, fishes[b][-1])
            break

    shark_move(sx, sy, sd, new_board, n, fishes)

def shark_move(sx, sy, sd, arr, n, f_arr):
    nsx, nsy = sx, sy
    success = True
    while(1):
        nsx, nsy = nsx + d[sd][0], nsy + d[sd][1]
        if nsx<0 or nsy<0 or nsx>=4 or nsy>=4:
            break
        if arr[nsx][nsy] != 0:    #물고기 존재
            success = False
            fn = arr[nsx][nsy]    #물고기 번호
            fx, fy, fd = f_arr[fn]
            arr[nsx][nsy], f_arr[fn] = 0, 0
            fishes_move(nsx, nsy, fd, arr, n+fn, f_arr)
            arr[nsx][nsy], f_arr[fn] = fn, (fx,fy,fd)

    if success:
        res.append(n)


d = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
fishes = [0 for _ in range(17)]
board = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    lst = list(map(int, input().split()))
    k = 0
    for j in range(0, 8, 2):
        fishes[lst[j]] = (i, k, lst[j+1]-1) #index : 물고기 번호, value : (행, 열, 방향)
        board[i][k] = lst[j]
        k+=1
fn = board[0][0]
sx, sy, sd = fishes[fn]
fishes[fn] = 0
board[0][0] = 0
res = []
fishes_move(sx, sy, sd, board, fn, fishes)
res.sort()

print(res[-1])