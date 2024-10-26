# 1. Test Case 모두 성공
# -> BUT 제출 시 Fail

import heapq

INF = int(1e9)
N, M = map(int, input().split()) # 방 개수, 통로 개수
S, E, C = map(int, input().split()) #시작 방 번호, 종료 방 번호, 한 번에 이동 가능한 사람 수 

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

result = -1
for i in range(M):
	a, b, k = map(int,input().split())
	graph[a].append([b,k])
	
def dijkstra(start,end):
	q = []
	heapq.heappush(q, (0,start)) # heapq에 (지불해야하는금액,종료지점) 넣기 
	distance[start] = 0
	while q:
		dist, endpos = heapq.heappop(q)
		
		# 1. dist까지
		# 이전에 저장한 비용이 더 작은 경우 코드 진행할 필요 없음
		if distance[endpos] < dist:
			continue
		# 비용 계산. 종료 지점은 같지만 비용이 다를 경우 가장 작은 비용이 들도록 함
		# 2. dist 이후
		for b, k in graph[endpos]:
			if C%k == 0:
				cost = dist + C//k
			else:
				cost = dist + (C//k) + 1
			
			if cost < distance[b]: #위에서 진행한 것보다 비용이 더 적게 들면 업데이트
				distance[b] = cost
				heapq.heappush(q, (cost, b))
		
		if endpos == E:
			return cost

result = dijkstra(S,E)

if result == -1:
	print(-1)
else:
	print(result)
	
# 2.