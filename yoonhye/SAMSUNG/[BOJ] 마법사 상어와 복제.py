#가장 왼쪽 윗 칸 : (1,1)
#둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마버사 상어와 물고기가 같은 칸에 있을 수도 있다.
#상어의 마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.
#1. 복제 마법 시전 (5번에서 복제되어 칸에 나타남)
#2. 모든 물고기가 한 칸 이동. (상어가 있는 칸, 물고기의 냄새가 있는 칸, 범위 벗어나는 칸으로는 이동 불가) 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전. 그래도 없으면 이동 X
#3. 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
#상어 이동 중 물고기가 있으면 그 칸에 있는 모든 물고기는 제외되고, 물고기 냄새를 남긴다. 가능한 이동 방법 중 제외되는 물고기의 수가 가장 많은 방법으로 이동하며 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용.
#4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
#5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
#S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
#상어 이동 방법 사전 순 : 상1 좌2 하3 우4. 수를 이어붙여 정수로 만들었을 때, a<b인 경우 A가 B보다 사전 순으로 앞선 것.
#물고기 방향 : 1~8 => 좌 좌상 상 우상 우 우하 하 좌하

from collections import deque
from collections import defaultdict

def permutation_with_repeat(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation_with_repeat(arr, r-1):
                yield [arr[i]] + next

M, S = map(int, input().split())
board = [[[] for _ in range(5)] for _ in range(5)]

fishes = defaultdict(list)
smell = deque([[],[]])
for _ in range(M):
    fx, fy, d = map(int, input().split())
    fishes[(fx,fy)].append(d)

sx, sy = map(int, input().split())
delta = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

shark_move_route = list(permutation_with_repeat([1,2,3,4], 3))
shark_move_direction = [(-1,0), (0,-1), (1,0), (0,1)]   #상,좌,하,우
for _ in range(S):
    #모든 물고기 한 칸 이동
    move_fishes = defaultdict(list)
    for x, y in fishes.keys():
        for fd in fishes[(x,y)]:
            initial_fd = fd
            while(1):
                nx, ny = x + delta[fd-1][0], y + delta[fd-1][1]
                if 1<=nx<=4 and 1<=ny<=4:
                    if (nx,ny) not in smell[0]+smell[1] and (nx,ny) != (sx,sy):  #물고기의 냄새가 없고, 상어가 없으면
                        move_fishes[(nx,ny)].append(fd)
                        break
                fd -= 1
                if fd == 0:
                    fd = 8
                if initial_fd == fd:    #물고기가 이동 못 했을 경우
                    move_fishes[(x, y)].append(fd)
                    break

    #상어가 연속해서 3칸 이동
    score = 555 #사전 순 확인을 위한 점수 초기값
    res_die_fishes = 0
    res = []    #최종적으로 상어가 이동한 경로
    for route in shark_move_route:
        move_sx, move_sy = sx, sy
        die_fishes = 0  # 상어가 지나가면서 제외된 물고기 수
        success = True
        new_score = route[0] * 100 + route[1] * 10 + route[2]
        visited = []
        for i in range(3):
            d = shark_move_direction[route[i]-1]
            nsx, nsy = move_sx + d[0], move_sy + d[1]
            if nsx < 1 or nsy < 1 or nsx > 4 or nsy > 4:
                success = False
                break
            if (nsx, nsy) not in visited :
                die_fishes += len(move_fishes.get((nsx, nsy), []))
                visited.append((nsx, nsy))
            move_sx, move_sy = nsx, nsy

        if (success) :  #상어가 3번 이동하는 데 성공했으면
            if (die_fishes > res_die_fishes) or (die_fishes == res_die_fishes and score > new_score):
                res_die_fishes = die_fishes
                score = new_score
                res = route[:]

    smell_route = []

    for i in res:
        sx, sy = sx+shark_move_direction[i-1][0], sy+shark_move_direction[i-1][1]
        if move_fishes.get((sx, sy)) != None:
            del move_fishes[(sx, sy)]    #상어가 이동한 경로의 물고기 제외
            smell_route.append((sx, sy))
    smell.pop() #두 번 전 연습에서 생긴 물고기의 냄새 제거
    smell.appendleft(smell_route)   #새롭게 추가된 물고기 냄새

    # 5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
    for key, value in move_fishes.items():
        fishes[key] += value

answer = 0
for value in fishes.values():
    answer += len(value)

print(answer)
