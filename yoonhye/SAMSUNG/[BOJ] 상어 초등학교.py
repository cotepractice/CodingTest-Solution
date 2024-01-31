#(1,1) ~ (N,N)
#인접한 칸 = 상하좌우 거리 1
#1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
#2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 칸으로 정한다.
#만족도 => 0, 1, 2, 3, 4 => 0, 1, 10, 100, 1000

from collections import deque

def find(n):
    global N
    d = [(-1,0), (1,0), (0,1), (0,-1)]
    num, index = (0, 0), (20, 20) #(인접한 칸에 존재하는 좋아하는 학생 수, 비어있는 칸 수), 좌표

    for x in range(N):
        for y in range(N):
            if board[x][y] :    #이미 학생이 있으면
                continue
            s_num, blank = 0, 0
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if board[nx][ny] == 0:
                    blank += 1
                elif board[nx][ny] in students[n]:
                    s_num += 1
            if num < (s_num, blank):
                num, index = (s_num, blank), (x, y)
            elif num == (s_num, blank):
                if index > (x,y):   #행, 열이 더 작으면
                    index = (x,y)
    board[index[0]][index[1]] = n

N = int(input())
students = dict()
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N**2):
    arr = list(map(int, input().split()))
    students[arr[0]] = arr[1:]

index = deque()
student_number = list(students.keys())
board[1][1] = student_number[0]
for n in range(1, N**2):
    find(student_number[n])

delta = [(-1,0), (1,0), (0,1), (0,-1)]
res = 0
score = [0, 1, 10, 100, 1000]
for x in range(N):
    for y in range(N):
        cnt = 0
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] in students[board[x][y]] :
                cnt+=1
        res += score[cnt]

print(res)