from collections import deque

def solution(sequence, k):
    queue = deque()
    sum = 0
    answer = [0, 1000000]
    for i in range(len(sequence)):
        queue.append(i)
        sum += sequence[i]
        while (sum > k):
            sum -= sequence[queue.popleft()]
        if sum == k:
            if queue[-1] - queue[0] < answer[-1] - answer[0]:
                answer = [queue[0], queue[-1]]

    return answer