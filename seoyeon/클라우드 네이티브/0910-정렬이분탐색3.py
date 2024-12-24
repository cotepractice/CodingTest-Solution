#1. 시간 초과
N = int(input())

singer_lst = list(map(int, input().split()))

singer_lst.sort(reverse=True) #내림차순

result = 0
for i in range(N-2):
	most = singer_lst[i]
	for j in range(i+1,N-1):
		second = singer_lst[j]
		for k in range(j+1,N):
			third = singer_lst[k]
			if most <= second+third:
				result += 1

print(result)

#2. 