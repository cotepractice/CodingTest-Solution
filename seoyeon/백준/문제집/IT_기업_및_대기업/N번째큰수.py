#백준 2075 N번째 큰 수


N = int(input()) #N번째 큰 수
lst = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    lst[i] = list(map(int, input().split()))

dict_lst = [-1 for _ in range(N)]
col = [(N-1) for _ in range(N)] #index

for i in range(N):
    last =  lst[N-1][i] #맨 뒤 숫자
    dict_lst[i] = last

#아래 반복
#1. dict에서 가장 큰 수 찾기
#2. 해당 수 위에 존재하는 수로 dict 업데이트

cnt = 0
while True:
    cnt += 1
    max_n = max(dict_lst)
    #print("max",max_n)
    for i in range(N):
        if dict_lst[i]==max_n:
            col[i] -= 1
            #print("dict_lst:",dict_lst,"lst:",lst,"col:",col)
            dict_lst[i] = lst[col[i]][i]
    if cnt == N:
        print(max_n)
        break