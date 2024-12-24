# 1. TestCase 1 성공. 2,3 실패
# -> 시작 지점에서 끝 지점으로 직접 연결되는 경우가 최단 경우인 경우 성립. BUT 우회하는 것이 최단거리일 수 있음. 해결필요

N, M = map(int, input().split())
S = int(input())
#lst = [[-1,-1,-1] for _ in range(M)]
weight_lst = [[0 for _ in range(N)] for _ in range(N)]
weight = [1e8 for _ in range(N)]

for i in range(M):
	s, e, w = map(int,input().split())
	weight_lst[s-1][e-1] = w 
	#lst[i] = [s,e,w]

# case1. 시작지점과 바로 연결된 경우
for target in range(N):
	if weight_lst[S-1][target] > 0:
		weight[target] = weight_lst[S-1][target]
#print("weight:",weight)
# case2. 
for i in range(N): #끝나는 정점
	if i == S-1:
		continue
	for j in range(N): #거치는 정점
		if j == S-1 or j == i:
			continue
		#print("First i:",i,"j:",j,weight_lst[j][i])
		if weight_lst[j][i] > 0 and weight[j]>0:
			#print("Second i:",i,"j:",j,weight_lst[j][i])
			weight[i] = min(weight[i], weight[j]+weight_lst[j][i])
			
#print(weight)
result = 0
check = 0
for i in range(N):
	if i==S-1:
		continue
	if weight[i]==1e8:
		check = 1 
		break
	else:
		result += weight[i]

if check == 0:
	print(result)
else:
	print(-1)
	
# 2. 시작 지점과 연결된 정점에서 각 정점까지의 최단 거리 탐색 후 최단거리 비교
# -> 테스트 케이스 성공. BUT 제출 시 실패

from collections import deque

N, M = map(int, input().split())
S = int(input())
weight_lst = [[1e8 for _ in range(N)] for _ in range(N)]
weight = [1e8 for _ in range(N)]
direct = deque([])

for i in range(M):
	s, e, w = map(int,input().split())
	
	weight_lst[s-1][e-1] = min(weight_lst[s-1][e-1], w) 
	if s == S:
		direct.append(e-1)

# case1. 시작지점과 바로 연결된 경우
for target in range(N):
	if weight_lst[S-1][target] > 0:
		weight[target] = min(weight[target], weight_lst[S-1][target])

# 시작지점에서 각 정점까지의 최단 거리 비교
while direct:
	direct_idx = direct.popleft() #시작지점
	for i in range(N): #종료지점
		if weight_lst[direct_idx][i] > 0:
			weight[i] = min(weight[i], weight_lst[S-1][direct_idx]+weight_lst[direct_idx][i])

# case2. 우회하는 것이 최단 거리인 경우
for i in range(N): #끝나는 정점
	if i == S-1:
		continue
	for j in range(N): #거치는 정점
		if j == S-1 or j == i:
			continue

		if weight_lst[j][i] > 0 and weight[j]>0:
			weight[i] = min(weight[i], weight[j]+weight_lst[j][i])
			
result = 0
for i in range(N):
	if i==S-1:
		continue
	if weight[i]==1e8:
		result -= 1
	else:
		result += weight[i]

print(result)

# 3. 성공
import sys
import heapq
 
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)] # index와 숫자를 맞춤. index 0은 힝상 []
distance = [INF] * (n + 1)
 
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

print("graph:",graph)

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start)) # q에 (도착지점,이동비용) 넣음
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if distance[now]<dist:	# 이전에 진행했을 때가 더 작으면 아래 코드 진행 X
			continue

		for b, c in graph[now]:
			cost = dist + c
			if cost < distance[b]: # 이전의 이동 비용보다 b를 거쳐가는 비용이 더 작은 경우 값 변경 
				distance[b] = cost
				heapq.heappush(q, (cost, b)) # q에 변경된 값을 다시 넣음


dijkstra(start)

result = 0

for i in range(1, n + 1):
	if distance[i] == INF:
		result -= 1
	else:
		result += distance[i]

print(result)