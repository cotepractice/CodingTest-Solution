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

# 3. 