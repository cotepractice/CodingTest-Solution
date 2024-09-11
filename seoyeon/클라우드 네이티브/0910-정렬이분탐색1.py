N = int(input())

pos_lst = [[-1,-1] for _ in range(N)]
result_lst = [0 for _ in range(N)]

for i in range(N):
	x, y = map(int, input().split())
	pos_lst[i] = [x,y,i]

pos_lst.sort(key=lambda x : (x[0], x[1]))
	
for i in range(N):
	result_lst[pos_lst[i][2]] = N-i-1

print(*result_lst, sep="\n")