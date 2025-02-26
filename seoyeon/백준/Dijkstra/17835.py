#백준 #17835 면접보는 승범이네
#Dijkstra
#시간초과 발생

import heapq

def dijkstra(start):
    global distance

    interview_d = float("inf") #최소거리

    heap = [[0,start]] #[cost,city]
    heapq.heapify(heap)
    distance[start] = 0

    while heap:
        cur_cost, cur_city = heapq.heappop(heap)

        if cur_city+1 in interview:
            interview_d = min(cur_cost,interview_d)

        if cur_cost > distance[cur_city]:
            continue

        for next_city,next_cost in roads[cur_city]:
            cost = cur_cost+next_cost
            if cost<distance[next_city]:
                distance[next_city]=cost
                heapq.heappush(heap,[cost,next_city])
    
    return interview_d

N,M,K = map(int,input().split())
roads = [[] for _ in range(N)]

for m in range(M):
    s,e,c = map(int,input().split())
    roads[s-1].append([e-1,c])

interview = list(map(int,input().split())) #면접장

min_d = [float("inf") for _ in range(N)]

ans_idx = -1
ans_d = -1

#city 0부터 N-1까지 탐색
for n in range(N):
    distance = [float("inf") for _ in range(N)] #거리
    ans_n = float("inf")
    small_d = dijkstra(n)
    if small_d>ans_d:
        ans_idx = n+1
        ans_d = small_d

print(ans_idx)
print(ans_d)