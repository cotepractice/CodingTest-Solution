# (1,1)부터 시작. => 나는 (0,0)부터 시작할거니까 주의하기
# 기사의 위치 (r,c)를 좌측 상단으로 하는 hXw 크기의 직사각형.
# 밀려난 기사들은 해당 기사가 이동한 곳에서 wxh 직사각형 내에 놓여 있는 함정의 수만큼 피해를 입는다.
# 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 대미지를 받을 경우 체스판에서 사라짐.
# 명령을 받은 기사는 피해 X. 기사들은 모두 밀린 이후에 대미지를 입는다.
# 생존한 기사들이 총 받은 대미지의 합 return


# 왼쪽으로 미는 경우
# (r,c) ~ (r+h-1, c) => 얘네를 밀었을 때 밀 수 있으면 가능

# 오른쪽
# (r,c+w-1) ~ (r+h-1, c+w-1)

# 위쪽
# (r, c) ~ (r, c+w-1)

# 아래쪽
# (r+h-1, c) ~ (r+h-1, c+w-1)


def check_move(n, d, can_move):
    global L
    r, c, h, w, k = info[n]

    # [열이 바뀜, (고정값, 바뀌는 값)] or [행이 바뀜, (바뀌는 값, 고정값)]
    loop_range = [["c", (0, w - 1)], ["r", (h - 1, w - 1)], ["c", (h - 1, w - 1)], ["r", (h - 1, 0)]]

    dx, dy = delta[d]

    other_knight = set()
    nr, nc = r + loop_range[d][1][0], c + loop_range[d][1][1]
    if loop_range[d][0] == "r":  # 열 고정, 행이 바뀜
        for i in range(r, nr + 1):
            x, y = i + dx, nc + dy
            if x < 0 or y < 0 or x >= L or y >= L or board[x][y] == 2:
                return False
            if knight[x][y] != n and knight[x][y] > 0:  # 다른 기사가 있으면
                other_knight.add(knight[x][y])

    else:  # 행 고정, 열이 바뀜
        for i in range(c, nc + 1):
            x, y = nr + dx, i + dy
            if x < 0 or y < 0 or x >= L or y >= L or board[x][y] == 2:
                return False
            if knight[x][y] != n and knight[x][y] > 0:  # 다른 기사가 있으면
                other_knight.add(knight[x][y])

    # 기사가 이동이 가능하다면 다음 기사도 이동이 되는지 확인
    can_move.append(n)
    for num in other_knight:
        # 하나라도 이동이 불가능한 경우 전체 이동 불가능
        if check_move(num, d, can_move) == False:
            return False

    return can_move


def change_knight_board(n, d, t):
    r, c, h, w, k = info[n]

    # [열이 바뀜, (고정값, 바뀌는 값)] or [행이 바뀜, (바뀌는 값, 고정값)]
    loop_range = [["c", (0, w - 1)], ["r", (h - 1, w - 1)], ["c", (h - 1, w - 1)], ["r", (h - 1, 0)]]

    dx, dy = delta[d]

    nr, nc = r + loop_range[d][1][0], c + loop_range[d][1][1]
    if loop_range[d][0] == "r":  # 열 고정, 행이 바뀜
        for i in range(r, nr + 1):
            x, y = i, nc
            if t == n:
                x, y = x + dx, y + dy
            knight[x][y] = t

    else:  # 행 고정, 열이 바뀜
        for i in range(c, nc + 1):
            x, y = nr, i
            if t == n:
                x, y = x + dx, y + dy
            knight[x][y] = t


def damage(n):
    r, c, h, w, k = info[n]
    cnt = 0
    for x in range(r, r + h):
        for y in range(c, c + w):
            if board[x][y] == 1:
                cnt += 1
    if k - cnt <= 0:
        del info[n]
        del init_damage[n]
        for x in range(r, r + h):
            for y in range(c, c + w):
                knight[x][y] = 0
    else:
        info[n][-1] = k - cnt


L, N, Q = map(int, input().split())

# 0 : 빈 칸, 1 : 함정, 2: 벽
board = [list(map(int, input().split())) for _ in range(L)]

init_damage = dict()
info = dict()
knight = [[0 for _ in range(L)] for _ in range(L)]
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r, c = r - 1, c - 1
    info[i] = [r, c, h, w, k]
    init_damage[i] = k
    for x in range(r, r + h):
        for y in range(c, c + w):
            knight[x][y] = i

# 명령 : (i,d) => i번 기사에게 d 방향으로 한 칸 이동하라는 명령
# 이미 사라진 기사의 번호가 주어질 수도 있다.
# d : 0~3 => 상, 우, 하, 좌
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌
req = []
for _ in range(Q):
    i, d = map(int, input().split())
    req.append((i, d))

for i, d in req:
    if info.get(i) == None:
        continue
    move_knights = check_move(i, d, [])
    if move_knights == False:
        continue
    # 이동 가능한 기사들을 이동시킴
    dx, dy = delta[d]

    for n in move_knights[::-1]:
        change_knight_board(n, d, n)
        other_d = (d + 2) % 4
        change_knight_board(n, other_d, 0)
        info[n][0], info[n][1] = info[n][0] + dx, info[n][1] + dy
    for n in move_knights[1:]:
        damage(n)

init_hp = sum(init_damage.values())
final_hp = 0
for n in info.keys():
    final_hp += info[n][-1]

print(init_hp - final_hp)
