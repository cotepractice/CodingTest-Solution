#1.격자를 2^L X 2^L 크기의 부분 격자로 나눈다.
#2.모든 부분 격자를 시계 방향으로 90도 회전시킨다.
#3.얼음이 있는 칸 3개 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
#인접한 칸 => 상하좌우
#남아있는 얼음의 합과 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수를 return

from collections import deque
def divide_and_rotate(n):
    global N
    new_board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(0, 2**N, n):
        for j in range(0, 2**N, n):
            for k in range(n):
                l = 0
                for v in board[i+k][j:j+n]:
                    new_board[i+l][j+n-1-k] = v
                    l+=1

    return new_board

def decrease_ice():
    global N
    new_board = [board[i][:] for i in range(2**N)]
    d = [(-1,0), (1,0), (0,-1), (0,1)]  #상하좌우
    for x in range(2**N):
        for y in range(2**N):
            if board[x][y] == 0 :
                continue
            cnt = 4 #인접한 칸에 얼음이 있는 경우 중 칸의 개수의 최댓값 (상하좌우)
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>=2**N or ny>=2**N:
                    cnt -= 1
                    continue
                if board[nx][ny] == 0 : #얼음이 없는 경우
                    cnt -= 1
                if cnt <= 2:
                    break
            if cnt <= 2:
                new_board[x][y] -= 1
    return new_board

def find_ice_set():
    global N
    visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
    d = [(-1,0), (1,0), (0,-1), (0,1)]  #상하좌우
    res = 0
    for i in range(2**N):
        for j in range(2**N):
            if visited[i][j] or board[i][j]==0 :  #방문한 적이 있거나 얼음이 없으면
                continue
            queue = deque([(i,j)])
            cnt = 0
            visited[i][j] = 1
            while(queue):
                x, y = queue.popleft()
                cnt += 1
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>=2**N or ny>=2**N:
                        continue
                    if board[nx][ny] and visited[nx][ny] == 0 :  #얼음이 있고 방문한 적이 없으면
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
            res = max(res, cnt)
    return res

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))

for q in range(Q):
    if L_list[q] != 0:
        n = 2 ** L_list[q]
        board = divide_and_rotate(n)
    board = decrease_ice()

total_ice = 0
ice_set_cnt = find_ice_set()
for arr in board:
    total_ice += sum(arr)

print(total_ice)
print(ice_set_cnt)


