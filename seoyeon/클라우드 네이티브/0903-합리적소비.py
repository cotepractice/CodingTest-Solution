N = int(input())

lst = [[0,0] for _ in range(N)]

for k in range(N):
	item, money = input().split()
	lst[k] = [item, int(money)]
	
lst.sort(key=lambda x: x[1])

print(*lst[N-1])
print(*lst[0])