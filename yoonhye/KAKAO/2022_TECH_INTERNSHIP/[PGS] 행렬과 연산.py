from collections import deque


def solution(rc, operations):
    M = len(rc[0])  # 열의 개수

    # 예외처리 (열이 2개만 있는 경우 - 런타임 에러 방지)
    if M == 2:
        first_col = deque()
        last_col = deque()
        for arr in rc:
            first_col.append(arr[0])
            last_col.append(arr[1])

        for op in operations:
            if op == "Rotate":
                last_col.appendleft(first_col.popleft())
                first_col.append(last_col.pop())
            else:
                first_col.appendleft(first_col.pop())
                last_col.appendleft(last_col.pop())
        result = []
        for fc, lc in zip(first_col, last_col):
            result.append([fc, lc])

    else:
        first_col = deque()
        last_col = deque()
        rc_deque = deque()
        for arr in rc:
            arr = deque(arr)
            first_col.append(arr.popleft())
            last_col.append(arr.pop())
            rc_deque.append(arr)

        for op in operations:
            if op == "Rotate":
                last_col.appendleft(rc_deque[0].pop())
                rc_deque[-1].append(last_col.pop())
                first_col.append(rc_deque[-1].popleft())
                rc_deque[0].appendleft(first_col.popleft())
            else:
                last_col.appendleft(last_col.pop())
                first_col.appendleft(first_col.pop())
                rc_deque.appendleft(rc_deque.pop())

        result = []
        for fc, arr, lc in zip(first_col, rc_deque, last_col):
            row = []
            row.append(fc)
            row.extend(arr)
            row.append(lc)
            result.append(row)
    return result
