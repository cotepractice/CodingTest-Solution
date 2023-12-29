def ShiftRow(rc, N):
    new_rc = [0] * N
    for i in range(N - 1):
        new_rc[i + 1] = rc[i]
    new_rc[0] = rc[-1]
    return new_rc


def Rotate(rc, N, M):
    new_rc = [item[:] for item in rc]
    for a in range(0, M - 1):  # 첫 행에서 끝 열에 있는 원소를 제외한 첫 행의 모든 원소는 오른쪽으로 한 칸 이동
        new_rc[0][a + 1] = rc[0][a]

    for b in range(0, N - 1):  # 끝 열에서 끝 행에 있는 원소를 제외한 끝 열의 모든 원소는 아래쪽으로 한 칸 이동
        new_rc[b + 1][-1] = rc[b][-1]

    for c in range(1, M):  # 끝 행에서 첫 열에 있는 원소를 제외한 끝 행의 모든 원소는 왼쪽으로 한 칸 이동
        new_rc[-1][c - 1] = rc[-1][c]

    for d in range(1, N):  # 첫 열에서 첫 행에 있는 원소를 제외한 첫 열의 모든 원소는 위쪽으로 한 칸 이동
        new_rc[d - 1][0] = rc[d][0]

    return new_rc


def solution(rc, operations):
    M = len(rc[0])  # 열의 개수
    N = len(rc)  # 행의 개수

    for op in operations:
        if op == "Rotate":
            rc = Rotate(rc, N, M)
        else:
            rc = ShiftRow(rc, N)

    return rc