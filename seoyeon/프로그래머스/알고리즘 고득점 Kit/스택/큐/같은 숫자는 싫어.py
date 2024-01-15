#프로그래머스 알고리즘 고득점 Kit
#스택/큐문제
#같은 숫자는 싫어

from collections import deque

def solution(arr):
    queue = deque(arr)
    n = len(arr)
    
    answer = []
    
    while queue:
        x = queue.popleft()
        if answer == []:
            answer.append(x)
            continue
        y = answer[-1]
        if (x != y):
            answer.append(x)
    
    
    return answer