# 6109 추억의 2048 게임
from collections import deque

def up():
    global matrix

    ans_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        Q = deque()
        prev = -1
        for i in range(N):
            #print("Q:",i, Q)
            #0은 입력으로 안받음
            if matrix[i][j] == 0:
                continue
            #초기값
            if prev==-1:
                prev = matrix[i][j]
                Q.append(prev)
                continue

            if prev == matrix[i][j]:
                q = Q.pop()
                q += q
                Q.append(q)
                prev = -1
            else:
                Q.append(matrix[i][j])
                prev = matrix[i][j]

        for i in range(len(Q)):
            ans_matrix[i][j] = Q.popleft()
    #print("ans_matrix: ",ans_matrix)
    for i in range(N):
        print(*ans_matrix[i],sep=" ",end="\n")
    return ans_matrix

def down():
    global matrix

    ans_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        Q = deque()
        prev = -1
        for i in range(N-1,-1,-1):
            #print("Q:",i, Q)
            #0은 입력으로 안받음
            if matrix[i][j] == 0:
                continue
            #초기값
            if prev==-1:
                prev = matrix[i][j]
                Q.append(prev)
                continue

            if prev == matrix[i][j]:
                q = Q.pop()
                q += q
                Q.append(q)
                prev = -1
            else:
                Q.append(matrix[i][j])
                prev = matrix[i][j]

        for i in range(N-1,N-len(Q)-1,-1):
            ans_matrix[i][j] = Q.popleft()
    #print("ans_matrix: ",ans_matrix)
    for i in range(N):
        print(*ans_matrix[i],sep=" ",end="\n")
    return ans_matrix


def right():
    global matrix

    ans_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        Q = deque()
        prev = -1
        for j in range(N-1,-1,-1):
            #print("Q:",i, Q)
            #0은 입력으로 안받음
            if matrix[i][j] == 0:
                continue
            #초기값
            if prev==-1:
                prev = matrix[i][j]
                Q.append(prev)
                continue

            if prev == matrix[i][j]:
                q = Q.pop()
                q += q
                Q.append(q)
                prev = -1
            else:
                Q.append(matrix[i][j])
                prev = matrix[i][j]

        for j in range(N-1,N-len(Q)-1,-1):
            ans_matrix[i][j] = Q.popleft()
    #print("ans_matrix: ",ans_matrix)
    for i in range(N):
        print(*ans_matrix[i],sep=" ",end="\n")
    return ans_matrix


def left():
    global matrix

    ans_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        Q = deque()
        prev = -1
        for j in range(N):
            #print("Q:",i, Q)
            #0은 입력으로 안받음
            if matrix[i][j] == 0:
                continue
            #초기값
            if prev==-1:
                prev = matrix[i][j]
                Q.append(prev)
                continue

            if prev == matrix[i][j]:
                q = Q.pop()
                q += q
                Q.append(q)
                prev = -1
            else:
                Q.append(matrix[i][j])
                prev = matrix[i][j]

        for j in range(len(Q)):
            ans_matrix[i][j] = Q.popleft()
    #print("ans_matrix: ",ans_matrix)
    for i in range(N):
        print(*ans_matrix[i],sep=" ",end="\n")
    return ans_matrix





T = int(input())

for t in range(1,T+1):
    N, move = input().split()
    N = int(N)

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        lst = list(map(int,input().split()))
        matrix[i] = lst
    
    print("#",t,sep="")
    if move=="up":
        up()
    if move=="down":
        down()
    if move=="right":
        right()
    if move=="left":
        left()