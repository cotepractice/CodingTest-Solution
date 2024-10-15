#이분탐색 시 bisect 사용
#조건: set으로 풀지 말 것
import bisect

N = int(input())

N_lst = list(map(int,input().split()))
N_lst.sort()

M = int(input())

for i in range(M):
	B = int(input())
	
	idx = bisect.bisect_left(N_lst,B)

	#idx가 0과 N 사이가 아닌 경우 N_lst[idx] 코드 동작 시 오류 발생하기 때문에 첫 번째 조건 존재
	#만약 N_lst에 B가 없는 경우, idx는 N_lst에 들어갈 적절한 인덱스를 추출하기에 두 번째 조건 존재
	if 0<=idx<N and N_lst[idx]==B:  
		print(1)
	else:
		print(0)