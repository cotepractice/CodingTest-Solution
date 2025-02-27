#백준 #17835 면접보는 승범이네
#1.Dijkstra
#모든 도시에서 본인 도시를 제외한 모든 도시로의 최단 거리 계산 
#시간초과 발생

# import heapq

# def dijkstra(start):
#     global distance

#     interview_d = float("inf") #최소거리

#     heap = [[0,start]] #[cost,city]
#     heapq.heapify(heap)
#     distance[start] = 0

#     while heap:
#         cur_cost, cur_city = heapq.heappop(heap)

#         if cur_city+1 in interview:
#             interview_d = min(cur_cost,interview_d)

#         if cur_cost > distance[cur_city]:
#             continue

#         for next_city,next_cost in roads[cur_city]:
#             cost = cur_cost+next_cost
#             if cost<distance[next_city]:
#                 distance[next_city]=cost
#                 heapq.heappush(heap,[cost,next_city])

#     return interview_d

# N,M,K = map(int,input().split())
# roads = [[] for _ in range(N)]

# for m in range(M):
#     s,e,c = map(int,input().split())
#     roads[s-1].append([e-1,c])

# interview = list(map(int,input().split())) #면접장

# min_d = [float("inf") for _ in range(N)]

# ans_idx = -1
# ans_d = -1

# #city 0부터 N-1까지 탐색
# for n in range(N):
#     distance = [float("inf") for _ in range(N)] #거리
#     ans_n = float("inf")
#     small_d = dijkstra(n)
#     if small_d>ans_d:
#         ans_idx = n+1
#         ans_d = small_d

# print(ans_idx)
# print(ans_d)

#2.Dijkstra
#면접장->도시로의 거리로 계산
import sys,heapq

input = sys.stdin.readline

def dijkstra():
    global distance

    heap = []
    heapq.heapify(heap)
    for interview in interviews:
        heapq.heappush(heap,[0,interview-1]) #[cost,city]
        distance[interview-1]=0

    while heap:
        cur_cost, cur_city = heapq.heappop(heap)

        #distance보다 큰 경우 탐색할 필요 없음
        if cur_cost>distance[cur_city]:
            continue
        
        for next_city,next_cost in roads[cur_city]:
            cost = cur_cost+next_cost
            if cost<distance[next_city]:
                distance[next_city]=cost
                heapq.heappush(heap,[cost,next_city])

N,M,K = map(int,input().split())
roads = [[] for _ in range(N)]
distance = [float("inf") for _ in range(N)]

for m in range(M):
    s,e,c = map(int,input().split()) #s -> e
    roads[e-1].append([s-1,c]) #단방향.원래는 roads[s-1].append([e-1,c])이지만, 반대로 면접장에서 도시로 갈 것이기 때문에 반대로 저장

interviews = list(map(int,input().split())) #면접장

dijkstra()
#print("distance",distance)

#min_d에서 가장 큰 값과 인덱스 출력
ans = [-1,-1] #[도시번호,거리]
for i in range(N):
    if distance[i]>ans[1]:
        ans[0]=i+1
        ans[1]=distance[i]

print(*ans,sep="\n")