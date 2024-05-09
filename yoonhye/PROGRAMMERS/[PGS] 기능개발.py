import math

def solution(progresses, speeds):
    answer = []
    time = []
    if len(progresses) == 0: return [0]
    for p, s in zip(progresses, speeds):
        time.append(math.ceil((100 - p) / s))

    stack = [time[0]]
    for t in time[1:]:
        if stack[0] >= t:
            stack.append(t)
        else:
            answer.append(len(stack))
            stack = [t]
    answer.append(len(stack))
    return answer