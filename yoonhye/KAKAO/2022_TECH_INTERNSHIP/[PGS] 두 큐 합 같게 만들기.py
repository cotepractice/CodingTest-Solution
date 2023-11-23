# 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주.
# 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수 return
# queue1, queue2는 정수 배열.

from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    total = sum1 + sum2
    if (total % 2 != 0):
        return -1

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    limit = len(queue1) * 3
    num = 0

    while (1):
        if (num > limit):
            return -1

        if (sum1 > sum2):
            num += 1
            v = queue1.popleft()
            sum2 += v
            sum1 -= v
            queue2.append(v)
        elif (sum1 < sum2):
            num += 1
            v = queue2.popleft()
            sum1 += v
            sum2 -= v
            queue1.append(v)
        else:
            return num