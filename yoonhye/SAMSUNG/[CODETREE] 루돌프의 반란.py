#(1,1)부터.
#기절해있거나 격자 밖으로 빠져나가 게임에서 탈락한 산타들은 움직일 수 없다.
#루돌프는 가장 가까운 산타를 향해 1칸 돌진 (게임에서 탈락하지 않은 산타 중에서. 기절한 산타한테는 돌진 가능)
#루돌프 => 상하좌우 대각선 총 8방향 가능
#가장 가까운 산타가 2명 이상이라면, r 좌표가 더 큰 산타를 향해 돌진. 그것도 같으면 c가 더 큰 산타
#산타는 1번부터 P번까지 순서대로 움직임. 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
#다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없다.
#움직일 수 있는 칸이 없으면 산타는 움직이지 않는다. & 루돌프로부터 가까워질 수 있는 방법이 없으면 움직이지 않는다.
#산타 => 상하좌우 가능. 가까워질 수 있는 방향이 여러개이면 '상우하좌' 순서.
#산타와 루돌프가 같은 칸에 있게 되면 충돌 발생.
#1. 루돌프가 움직여서 충돌이 일어난 경우 => 그 산타는 C만큼의 점수 획득 & 산타는 루돌프가 이동해온 방향으로 C칸만큼 밀려남
#2. 산타가 움직여서 충돌 발생 => 그 산타는 D만큼의 점수 획득 & 산타는 자신이 이동해온 반대 방향으로 D칸 만큼 밀려남
#밀려나는 와중에 충돌이 발생하지 X. 밀려난 위치가 게임판 밖 -> 산타 탈락. 다른 산타가 있음 -> 상호작용
#산타가 충돌 후 밀려나서 착지하게 되는 칸에 다른 산타가 있으면 그 산타는 1칸 해당 방향으로 밀려남. 그 옆에 산타가 있으면 연쇄적으로 1칸씩 밀려남 (게임판에서 밀려나면 탈락)
#산타는 루돌프와 충돌 후 1턴 기절.
#if. P명의 산타가 모두 게임에서 탈락하게 되면 그 즉시 게임 종료. 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩 점수 부여
#게임이 끝났을 때 각 산타가 얻은 최종 점수를 구해라.

from collections import deque
def distance(r1,c1,r2,c2):
    return (((r1-r2)*(r1-r2)) + ((c1-c2)*(c1-c2)))

def crash(Rr, Rc, dx, dy, n, S): #루돌프 좌표(=충돌한 산타 좌표), 방향, 산타 번호, 점수
    global santa_number

    sx, sy = Rr, Rc
    score[n] += S  # 그 산타는 S만큼의 점수 획득
    board[sx][sy] = 0
    # 산타는 루돌프가 이동해온 방향으로 S칸 밀려남
    sx += (dx * S)
    sy += (dy * S)
    if sx < 1 or sy < 1 or sx > N or sy > N:  # 산타 탈락
        santa[n][-1] = 0
        santa_number -= 1
    else:  # 산타 기절
        santa[n] = [distance(Rr, Rc, sx, sy), sx, sy, 3]
        if (board[sx][sy]):  # 그 자리에 산타가 있다는 뜻
            nx, ny, num = sx, sy, n
            while (1):  # 산타가 없을 때까지 반복
                p = board[nx][ny]
                board[nx][ny] = num
                if p == 0:
                    break
                mx, my = nx + dx, ny + dy
                if mx < 1 or my < 1 or mx > N or my > N:  # 산타 탈락
                    santa[p][-1] = 0
                    santa_number -= 1
                    break
                else:
                    santa[p][0], santa[p][1], santa[p][2] = distance(Rr, Rc, mx, my), mx, my
                    num = p
                    nx, ny = mx, my
        else:  # 그 자리에 산타 없음
            board[sx][sy] = n
def r_move(Rr, Rc): #루돌프의 움직임
    global C, N
    d, sx, sy = 3000, 0, 0

    for i in range(1, len(santa)):
        if santa[i][-1]!=0:
            if (santa[i][0]<d) or (santa[i][0]==d and (santa[i][1], santa[i][2]) > (sx,sy)):
                d, sx, sy, status = santa[i]
                n = i
    x, y = (Rr-sx), (Rc-sy)
    dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]    #좌측부터 시계방향으로 0~7
    if x<0:
        if y<0: #우하향 대각선
            nRr, nRc, direction = Rr+1, Rc+1, 5
        elif y==0:  #아래
            nRr, nRc, direction = Rr+1, Rc, 6
        else :  #y>0. 좌하향
            nRr, nRc, direction = Rr+1, Rc-1, 7
    elif x>0:
        if y<0:  # 우상향 대각선
            nRr, nRc, direction = Rr-1, Rc+1, 3
        elif y==0:  # 위
            nRr, nRc, direction = Rr-1, Rc, 2
        else:  # y>0. 좌상향
            nRr, nRc, direction = Rr-1, Rc-1, 1
    else :  #x==0
        if y>0: #왼쪽
            nRr, nRc, direction = Rr, Rc-1, 0
        elif y<0:   #오른쪽
            nRr, nRc, direction = Rr, Rc+1, 4

    if (nRr,nRc) == (sx, sy):   #산타와 충돌이 일어난 경우
        crash(nRr, nRc, dir[direction][0], dir[direction][1], n, C)

    return (nRr, nRc)

def s_move(Rr, Rc):   #산타의 움직임
    global N, D
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
    for i in range(1, len(santa)):
        if (santa[i][-1] == 1) :
            success = False
            d = santa[i][0]
            dir_x, dir_y = 0, 0
            for dx, dy in delta:
                nx, ny = santa[i][1]+dx, santa[i][2]+dy
                if nx<1 or ny<1 or nx>N or ny>N or board[nx][ny]:
                    continue
                if distance(Rr, Rc, nx, ny) < d :
                    d = distance(Rr, Rc, nx, ny)
                    success = True
                    mx,my, dir_x, dir_y = nx,ny,dx,dy
            if success:
                board[santa[i][1]][santa[i][2]] = 0
                if d==0:    #산타와 루돌프가 충돌한 경우
                    crash(Rr, Rc, -dir_x, -dir_y, i, D)
                else:
                    board[mx][my] = i
                    santa[i][0], santa[i][1], santa[i][2] = distance(Rr, Rc, mx, my), mx, my


N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())  #루돌프의 초기 위치
score = dict()
santa = [0 for _ in range(P+1)]
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
santa[0] = [0,0,0,0]
santa_number = P
for _ in range(P):
    Pn, Sr, Sc = map(int, input().split())
    santa[Pn] = [distance(Rr,Rc,Sr,Sc), Sr, Sc, 1]   #[루돌프와 산타의 거리, r, c, 상태]. 상태 0(탈락), 1(생존), 2,3(기절)
    board[Sr][Sc] = Pn
    score[Pn] = 0

for t in range(M):
    if (santa_number == 0):
        break
    Rr, Rc = r_move(Rr,Rc)
    for k in range(1, P+1):
        if (santa[k][-1]):  #탈락 안 했으면
            santa[k][0] = distance(Rr, Rc, santa[k][1], santa[k][2])

    s_move(Rr, Rc)
    for i in range(1, P+1):
        if santa[i][-1] != 0:   #탈락하지 않은 산타이면
            score[i] += 1
            if santa[i][-1] != 1:   #기절한 산타이면
                santa[i][-1] -= 1

for i in range(1, P+1):
    print(score[i], end=" ")

