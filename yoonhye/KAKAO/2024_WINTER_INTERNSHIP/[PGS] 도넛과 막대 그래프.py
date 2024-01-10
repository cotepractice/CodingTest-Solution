# 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수 return
# 나가면 +, 들어오면 - 해서 최종적으로 +가 가장 큰 번호가 생성한 정점
# 생성한 정점을 찾은 뒤 그 정점과 연결된 곳에서 출발해서 중복 지점이 2 이상이면 8자 모양, 1이면 도넛 모양, 0이면 막대 모양.
from collections import defaultdict

def solution(edges):
    score = defaultdict(int)
    graph = defaultdict(list)
    num = defaultdict(int)
    for a, b in edges:
        score[a] += 1
        score[b] -= 1
        num[a], num[b] = 0, 0
        graph[a].append(b)
    dicts = dict(zip(score.values(), score.keys()))
    new_node = dicts[max(dicts)]  # 생성한 정점

    donut, bar, eight = 0, 0, 0

    while (graph[new_node]):
        start = graph[new_node].pop()
        count = 0
        num[start] = 1
        while (graph[start]):
            if len(graph[start]) >= 2:
                count = 2
                break
            next = graph[start].pop()
            if num[next] == 0:
                num[next] = 1
            else:  # 이미 방문한 적이 있던 노드라면
                count += 1
            start = next

        if count >= 2:
            eight += 1
        elif count == 1:
            donut += 1
        else:
            bar += 1

    answer = [new_node, donut, bar, eight]
    return answer