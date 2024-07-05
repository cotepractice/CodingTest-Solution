# 나가면 +1, 들어오면 -1
from collections import defaultdict

def find_shape(graph, n):
    num = n
    while (1):
        if len(graph[num]) == 2:
            return 3
        elif len(graph[num]) == 0:
            return 2
        num = graph[num].pop()
        if num == n:
            return 1


def solution(edges):
    answer = [0] * 4
    graph = defaultdict(list)
    score = defaultdict(int)

    for x, y in edges:
        graph[x].append(y)
        score[x] += 1
        score[y] -= 1

    new_node = 0
    new_node_score = 0
    for key, value in score.items():
        if value > new_node_score:
            new_node = key
            new_node_score = value

    answer[0] = new_node
    for n in graph[new_node]:
        answer[find_shape(graph, n)] += 1

    return answer