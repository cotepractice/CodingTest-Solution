from collections import deque

def solution(rc, operations):
    M = len(rc[0])  # 열의 개수
    N = len(rc)  # 행의 개수
    start = 0
    end = N - 1

    rc_deque = deque([])
    for arr in rc:
        rc_deque.append(deque(arr))

    for op in operations:
        if op == "Rotate":
            # 첫 열 : popleft해서 한 행 위에 appendleft
            # 마지막 열 : pop해서 한 행 밑에 append
            for i in range(1, N):
                rc_deque[i - 1].appendleft(rc_deque[i].popleft())
                rc_deque[N - i].append(rc_deque[N - i - 1].pop())
        else:
            rc_deque.appendleft(rc_deque.pop())

    result = []
    for deq in rc_deque:
        result.append(list(deq))
    return result