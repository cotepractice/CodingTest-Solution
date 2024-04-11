# (1,1)부터 시작
# 벽은 회전할 때 내구도가 1씩 깎이며, 내구도가 0이 되면 빈 칸으로 변경된다.
# 모든 참가자는 동시에 움직인다.
# 우선순위 : 상하
# 이동을 끝낸 후, 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다. 더 위쪽에 있을 수록, 더 왼쪽에 있을수록 우선됨.
# 선택된 정사각형은 시계방향으로 90도 회전. 회전된 벽은 내구도가 1씩 깎인다.

# 최단거리 반환 함수
def shortest_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# 참가자 이동 함수
def move(ex, ey):
    global move_cnt, N
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new_participant = []
    for x, y in participant:
        d = shortest_distance(x, y, ex, ey)
        mx, my = x, y
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] > 0:
                continue

            if (nx, ny) == (ex, ey):
                move_cnt += 1
                mx, my = nx, ny
                break
            elif shortest_distance(nx, ny, ex, ey) < d:
                d = shortest_distance(nx, ny, ex, ey)
                mx, my = nx, ny

        if (mx, my) != (x, y) and (mx, my) != (ex, ey):  # 탈출이 아닌 이동을 했으면
            new_participant.append((mx, my))
            move_cnt += 1
        elif (mx, my) == (x, y):  # 이동을 안 했으면
            new_participant.append((mx, my))

    return new_participant


# 정사각형 한 변의 길이를 찾는 함수
def find_length(x1, y1, x2, y2):
    x1x2 = abs(x1 - x2)
    y1y2 = abs(y1 - y2)

    if x1x2 < y1y2:
        return (y1y2 + 1, "상하", y1y2 - x1x2)  # 정사각형 한 변의 길이, 정사각형이 되기 위해 늘려야 하는 방향, 늘려야 하는 길이
    elif x1x2 > y1y2:
        return (x1x2 + 1, "좌우", x1x2 - y1y2)
    else:  # x1x2 == y1y2. (x1, y1), (x2, y2)가 정사각형의 꼭짓점이라서 정사각형을 만들 필요가 없음
        return (x1x2 + 1, "", 0)


# 가장 작은 정사각형 찾는 함수
def find_smallest_square(ex, ey):
    sn = 11
    sr, sc = 11, 11
    for x, y in participant:
        n, direction, l = find_length(x, y, ex, ey)  # 정사각형 한 변의 길이
        if n <= sn:
            r, c = min((x, y), (x, ey), (ex, y), (ex, ey))
            if direction == "상하":
                for _ in range(l):
                    if r - 1 >= 0:
                        r -= 1
                    else:
                        break
            elif direction == "좌우":
                for _ in range(l):
                    if c - 1 >= 0:
                        c -= 1
                    else:
                        break

            if n < sn:
                sn = n
                sr, sc = r, c
            elif n == sn and (r, c) < (sr, sc):
                sr, sc = r, c
    return sn, sr, sc


# 회전
def rotate(arr):
    n = len(arr)
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    k = n - 1
    for i in range(n):
        lst = arr[i][:]
        for j in range(n):
            new_arr[j][k] = lst[j]
        k -= 1
    return new_arr


# 회전할 정사각형 추출 후 회전
def maze_rotate(n, r, c):
    new_board = []
    for i in range(r, r + n):
        lst = []
        for j in range(c, c + n):
            lst.append(board[i][j])
        new_board.append(lst)
    new_board = rotate(new_board)

    for i in range(r, r + n):
        for j in range(c, c + n):
            if new_board[i - r][j - c] > 0:  # 벽이면 내구도 1 감소
                new_board[i - r][j - c] -= 1
            elif new_board[i - r][j - c] == -1:  # 출구인 경우
                ex, ey = i, j
            board[i][j] = new_board[i - r][j - c]

    # 참가자 위치 회전
    for i in range(len(participant)):
        x, y = participant[i]
        if r <= x <= r + n - 1 and c <= y <= c + n - 1:
            participant[i] = (r + (y - c), (c + n - 1) - (x - r))

    return (ex, ey)


def pretty_print():
    global N
    for i in range(N):
        print(board[i])


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
participant = []
for i in range(M):
    a, b = map(int, input().split())
    participant.append((a - 1, b - 1))

ex, ey = map(int, input().split())
ex, ey = ex - 1, ey - 1  # 출구의 좌표
board[ex][ey] = -1

move_cnt = 0  # 참가자들의 이동 거리 합

for _ in range(K):
    participant = move(ex, ey)
    if not participant:  # 참가자가 모두 탈출함
        break

    n, r, c = find_smallest_square(ex, ey)
    ex, ey = maze_rotate(n, r, c)

print(move_cnt)
print(ex + 1, ey + 1)