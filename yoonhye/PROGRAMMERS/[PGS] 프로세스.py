from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque(enumerate(priorities))
    order = sorted(priorities)
    cnt = 1
    while (queue):
        i, p = queue.popleft()
        if order[-1] == p:
            if i == location:
                return cnt
            order.pop()
            cnt += 1
        else:
            queue.append((i, p))
    return cnt