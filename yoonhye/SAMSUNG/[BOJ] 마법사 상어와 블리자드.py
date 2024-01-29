#(1,1) ~ (N,N). N은 항상 홀수
#상하좌우 1~4. 상어는 di방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
#어떤 칸 A의 번호보다 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동. -> 더 이상 구슬이 이동하지 않을 때까지 반복. (그냥 계속 안 쪽을 빈 칸 없이 채움)
#4개 이상 연속하는 구슬이 있을 때 폭발. -> 구슬 이동 -> 구슬 폭발 -> ... 더 이상 폭발하는 구슬이 없을 때까지 반복.
#연속하는 구슬은 하나의 그룹. -> 1번 칸부터 차례대로 A,B 순서로 다시 칸에 들어감. (A : 그룹에 들어있는 구슬의 개수, B : 구슬의 번호)
#만약 구슬이 칸의 수보다 많아 칸에 다 들어가지 못하면 못 들어간 구슬은 사라짐. (무조건 짝수개라서 A,B 쌍은 같이 들어가거나 같이 빠짐)
#1X(폭발한 1번 구슬의 개수) + 2X(폭발한 2번 구슬의 개수) + 3X(폭발한 3번 구슬의 개수)
# 전체 : 8, 16, 24, 32, 40, ..., n+8
# 아래 : 2, 5, 8, ..., n+3
# 왼쪽 : 0, 1, 2, ..., n+1
# 오른쪽 : 4, 9, 14, ..., n+5
# 위 : 6, 13, 20, ..., n+7
from collections import deque
def make_snake_board(N):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    snake_board = list()
    x, y = N // 2, N // 2

    # 뱀 형태로 보드를 나눔
    for i in range(2, N, 2):
        arr = deque()
        x -= 1
        y -= 1
        for dx, dy in direction:
            for k in range(i):
                x += dx
                y += dy
                if board[x][y] != 0:
                    arr.append(board[x][y])
        snake_board.append(arr)
    return snake_board
def move():
    global N
    i = 0
    for n in range(8, ((N//2)*8) + 1, 8):
        v = n - len(board_queue[i])
        if i == N//2 - 1:   #마지막 인덱스이므로 더이상 뒤쪽에서 구슬을 가져올 수 없음
            return
        for _ in range(v):
            if (board_queue[i+1]):
                board_queue[i].append(board_queue[i+1].popleft())   #안 쪽을 빈 칸 없이 채움
            else:   #더이상 뒤쪽에 구슬이 존재하지 않음
                return
        i += 1

def bomb(): #폭발 & 구슬 이동
    global N
    new_board = [deque() for _ in range(N//2)]
    bomb_list = deque()
    length, k = 8, 0
    is_bomb = False
    for i in range(len(board_queue)):
        while(board_queue[i]):
            n = board_queue[i].popleft()
            if not bomb_list:   #bomb_list가 비어있으면
                bomb_list.append(n)
            elif n == bomb_list[-1]:
                bomb_list.append(n)
            else:
                if len(bomb_list) >= 4:
                    result[bomb_list[-1]] += len(bomb_list)
                    is_bomb = True
                else:   #4개 이상 연속하지 않아서 폭발하지 않는다.
                    while(bomb_list):
                        if len(new_board[k]) == length:
                            k += 1
                            length += 8
                        new_board[k].append(bomb_list.popleft())
                bomb_list = deque()
                bomb_list.append(n)

    if len(bomb_list) >= 4:
        result[bomb_list[-1]] += len(bomb_list)
        is_bomb = True
    else :
        while (bomb_list):
            if len(new_board[k]) == length:
                k += 1
                length += 8
            new_board[k].append(bomb_list.popleft())
    return (is_bomb, new_board)

def change():
    global N
    new_board = [deque() for _ in range(N // 2)]
    length, k = 8, 0
    group = []
    for i in range(len(board_queue)):
        while(board_queue[i]):
            n = board_queue[i].popleft()
            if not group:   #group이 비어있으면
                group.append(n)
            elif n == group[-1]:
                group.append(n)
            else:
                if len(new_board[k]) == length:
                    k += 1
                    length += 8
                if length > (N//2)*8 :
                    return new_board
                new_board[k].append(len(group)) #A : 그룹에 들어있는 구슬의 개수
                new_board[k].append(group[-1])  #B : 그룹을 이루고 있는 구슬의 번호
                group = []
                group.append(n)
    if len(new_board[k]) == length:
        k += 1
        length += 8
    if length > (N // 2) * 8:
        return new_board
    if group:
        new_board[k].append(len(group))
        new_board[k].append(group[-1])
    return new_board

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_queue = make_snake_board(N)    #보드를 뱀 형태로 나눠서 저장

queue = deque()
for i in range(M):
    queue.append((map(int, input().split())))
result = {1:0, 2:0, 3:0}
delta = [(6,7), (2,3), (0,1), (4,5)]  #상하좌우. (시작점, 차이)
for t in range(M):
    #구슬 파괴
    d, s = queue.popleft()
    index, dt = delta[d-1]
    for i in range(s):
        if len(board_queue[i]) >= index+1:
            del board_queue[i][index]
            index += dt
        else:
            break
    move()  #구슬 이동

    #구슬 폭발
    is_bomb = True
    while(is_bomb):
        is_bomb, board_queue = bomb()

    #구슬 변화
    board_queue = change()

answer = 1*result[1] + 2*result[2] + 3*result[3]
print(answer)