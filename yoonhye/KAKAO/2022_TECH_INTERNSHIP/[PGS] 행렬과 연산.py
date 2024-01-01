from collections import deque

def Rotate(rc, N, M):
    row = [rc[0][:], rc[-1][:]]  # 첫 행, 마지막 행

    column = [[], []]  # 첫 열, 마지막 열
    for k in range(N):
        column[0].append(rc[k][0])
        column[1].append(rc[k][-1])

    rc[0][1] = row[0][0]
    rc[-1][M - 2] = row[1][M - 1]
    for i in range(1, M - 1):
        rc[0][i + 1] = row[0][i]
        rc[-1][i - 1] = row[1][i]

    rc[1][-1] = row[0][-1]
    rc[N - 2][0] = row[1][0]
    for j in range(1, N - 1):
        rc[j + 1][-1] = column[1][j]
        rc[j - 1][0] = column[0][j]
    return rc


def solution(rc, operations):
    M = len(rc[0])  # 열의 개수
    N = len(rc)  # 행의 개수
    start = 0
    end = N - 1
    rc = deque(rc)
    for op in operations:
        if op == "Rotate":
            rc = Rotate(rc, N, M)
        else:
            rc.appendleft(rc.pop())

    return list(rc)
