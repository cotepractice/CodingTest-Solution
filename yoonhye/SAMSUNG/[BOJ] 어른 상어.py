#1의 번호를 가진 어른 상어는 가장 강력해서 모두를 쫓아낼 수 있음
#먼저, 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
#그 후 1초마다 모든 상어가 "동시에" 상하좌우로 인접한 칸 중 하나로 이동, 자신의 냄새를 그 칸에 뿌림. 냄새는 상어가 k번 이동하고 나면 사라진다.
#인접한 칸 중 아무 냄새가 없는 칸의 방향으로 이동 방향 결정. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡음.
#모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
#1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구해라
#1~4 => 상하좌우 => 코드에서 0~3으로 변경
from collections import defaultdict

def shark_move():
    global N, K
    moved_sharks = dict()

    for num, info in list(sharks.items()):  #1번 상어부터 순서대로 진행
        x, y, d = info
        rx, ry, rd = -1, -1, -1
        for dn in priority_direction[num][d]:
            dx, dy = dir[dn]
            nx, ny = x+dx, y+dy

            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if smell.get((nx,ny)) == None:  #아무 냄새도 없으면
                rx, ry, rd = nx, ny, dn
                break
            elif (rx,ry) == (-1,-1) and smell[(nx,ny)][0] == num:   #자신의 냄새가 있으면
                rx, ry, rd = nx, ny, dn

        if moved_sharks.get((rx, ry)) != None:   #이미 더 강한 상어가 해당 칸에 존재하면
            del sharks[num] #해당 상어 삭제
        else:
            moved_sharks[(rx, ry)] = (num, rd)

    for index, info in moved_sharks.items():
        sharks[info[0]] =(index[0],index[1], info[1])
        smell[index] = (info[0], K+1)


def smell_minus():
    for key, value in list(smell.items()):
        if value[1] == 1:
            del smell[key]
            continue
        smell[key] = (value[0], value[1]-1)

N, M, K = map(int, input().split())
board = []
smell = dict()
sharks = dict.fromkeys([int(x) for x in range(1,M+1)])

for i in range(N):
    board.append(list(map(int, input().split())))

initial_dir = list(map(lambda x : int(x)-1, input().split()))

dir = [(-1,0), (1,0), (0,-1), (0,1)]  #상하좌우
priority_direction = defaultdict(list)  #각 상어의 방향 우선순위 저장
for i in range(1, M+1):
    for j in range(4):
        priority_direction[i].append(list(map(lambda x : int(x)-1, input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j]: #상어가 존재하면 냄새를 남김
            n = board[i][j]
            smell[(i,j)] = (n, K)  #상어 번호, 카운트
            sharks[n] = (i,j,initial_dir[n-1])    #key: 상어 번호, value : 상어 좌표값, 방향

sec = 0
for _ in range(1001):
    sec += 1

    shark_move()
    smell_minus()

    if len(sharks) == 1:
        break

sec = sec if sec<=1000 else -1
print(sec)
