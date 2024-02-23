#파이어볼 방향 0~7 => (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)
#1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다. (같은 칸에 여러 개의 파이어볼이 존재할 수도 있다)
#2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서 다음과 같은 일이 일어난다.
#   (1). 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
#   (2). 파이어볼은 4개의 파이어볼로 나누어진다.
#   (3). 나누어진 파이어볼 =>
#       질량: (질량 합)//5,
#       속력 : (속력 합)//(합쳐진 파이어볼 개수),
#       방향 : 모두 홀수 or 모두 짝수이면 방향은 (0,2,4,6)이 되고, 그렇지 않으면 (1,3,5,7)이 된다.
#   (4). 질량이 0인 파이어볼은 소멸되어 없어진다.
#마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

from collections import defaultdict
N, M, K = map(int, input().split())
board = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[(r-1,c-1)].append((m,d,s))
delta = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

for t in range(K):
    new_board = defaultdict(list)
    more_than_two = set()
    for x, y in board.keys():
        for m,d,s in board[(x,y)]:
            dx, dy = delta[d]
            nx, ny = x+(dx*s), y+(dy*s)
            if nx<0:
                qx = abs(nx) // N
                if abs(nx) % N == 0:
                    qx -= 1
                nx = (qx+1) * N + nx
            else:
                nx = nx%N
            if ny < 0:
                qy = abs(ny) // N
                if abs(ny) % N == 0:
                    qy -= 1
                ny = (qy + 1) * N + ny
            else:
                ny = ny%N

            if new_board.get((nx,ny)) != None:
                more_than_two.add((nx,ny))
            new_board[(nx,ny)].append((m,d,s))

    for x, y in more_than_two:
        m_lst, d_lst, s_lst = zip(*new_board[(x,y)])
        new_m, new_s = sum(m_lst)//5, sum(s_lst)//(len(new_board[(x,y)]))
        new_board[(x, y)] = []
        if new_m == 0:
            continue
        if all(k%2 == 0 for k in d_lst) or all(k%2!=0 for k in d_lst):
            for i in range(0,7,2):
                new_board[(x,y)].append((new_m, i, new_s))
        else:
            for i in range(1,8,2):
                new_board[(x, y)].append((new_m, i, new_s))

    board = new_board

res = 0
for lst in board.values():
    for m,d,s in lst:
       res += m

print(res)