N, M = map(int,input().split())

lines = [[-1,-1] for _ in range(M)]
check = [0 for _ in range(N)] #해당 폭탄에 연결된 전선 수 

for i in range(M):
	a, b = map(int,input().split())
	lines[i] = [a-1,b-1]
	check[a-1] += 1 
	check[b-1] += 1

result = []

#만약 check[s]==1인 경우는 해당 전선 자르면 폭발하므로 안전한 전선이 아님 ㅂ!
for i in range(M):
	a,b = lines[i]
	if check[a]==1 or check[b]==1:
		continue
	else:
		result.append(i+1)
	
if len(result)==0:
	print(-1)
else:
	print(*result)
	