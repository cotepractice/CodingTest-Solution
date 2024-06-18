from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    rest_weight = weight
    queue = deque([0 for _ in range(bridge_length)])

    for tw in truck_weights:
        if rest_weight >= tw:
            rest_weight += queue.popleft()
            queue.append(tw)
            answer += 1
            rest_weight -= tw
        else:
            while (1):
                answer += 1
                rest_weight += queue.popleft()
                if (rest_weight >= tw):
                    rest_weight -= tw
                    queue.append(tw)
                    break
                queue.append(0)

    answer += bridge_length

    return answer