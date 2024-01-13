#프로그래머스 알고리즘 고득점 Kit
#스택/큐문제
#올바른 괄호

from collections import deque

def solution(s):
    answer = True
    
    queue = deque()
    
    for x in s:
        if x=="(":
            queue.append(0)
        else:
            if (queue == deque([])):
                return False

            queue.popleft()

    if (queue != deque([])):
        return False

    return True