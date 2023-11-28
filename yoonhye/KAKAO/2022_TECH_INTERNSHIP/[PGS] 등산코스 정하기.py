# 출입구, 쉼터, 산봉우리
# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간 => intensity
# 쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있다. => 연속적으로 휴식없는 이동이 발생하지 X.
# 특정 출입구에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 다시 원래의 출입구로 돌아오는 등산코스.
# 출입구 = 처음, 끝 각각 한 번씩. 산봉우리 = 한 번만
# intensity가 최소가 되도록 등산코스를 정한다.
# intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호와 intensity의 최솟값을 차례대로 정수 배열에 담아 return
# 등산코스가 여러 개라면, 그 중 산봉우리의 번호가 가장 낮은 등산코스 선택
# 임의의 두 지점 사이에 이동 가능한 경로가 항상 존재.
# 1<=w<= 10,000,000

import heapq

def solution(n, paths, gates, summits):
    info = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        info[a].append((b, c))  #a -> b까지 걸리는 시간 c
        info[b].append((a, c))  #b -> a까지 걸리는 시간 c
    INF = int(1e9)
    intensity = [(INF) for _ in range(n+1)]
    queue = []
    isSummit = [False for _ in range(n+1)]
    for summit in summits:
        isSummit[summit] = True
    for start in gates:
        intensity[start] = 0
        heapq.heappush(queue, (0, start))

    while queue :
        cost, a = heapq.heappop(queue)    #현재 노드까지의 최소 intensity, 현재 노드
        if (isSummit[a] or (intensity[a] < cost)):
            continue
        for b, c in info[a]:    #현재노드 a와 인접한 노드 b, a에서 b까지 가는 데 걸리는 시간 c
            if (intensity[b] > max(cost, c)):
                intensity[b] = max(cost, c)
                heapq.heappush(queue, (intensity[b], b))

    res_summit = INF
    res_intensity = INF
    summits.sort()
    for summit in summits:
        if intensity[summit] < res_intensity:
            res_intensity = intensity[summit]
            res_summit = summit
    return [res_summit, res_intensity]