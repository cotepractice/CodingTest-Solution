#SWExpertAcademy 1267 작업순서
from collections import deque

def dfs(start_v):
    global dp,visited,cnt

    Q = deque(start_v)
    count_n = 0
    ans_lst = []
    while Q:
        count_n += 1
        
        x = Q.popleft()
        ans_lst.append(x)

        if count_n==V:
            return ans_lst
        
        #해당 좌표가 갈 수 있는 정점의 cnt 감소
        for i in range(V):
            if dp[x][i]==True:
                cnt[i] -= 1

        #다음에 갈 정점 탐색
        for i in range(V):
            if dp[x][i]==True and visited[i]==False and cnt[i]==0:
                dp[x][i]=False
                visited[i]=True
                Q.append(i)
        
        

for t in range(1,11):
    V,E = map(int,input().split())
    e_lst = list(map(int,input().split()))
    dp = [[False for _ in range(V)] for _ in range(V)] #dp[x][y]는 x->y
    cnt = [0 for _ in range(V)] #정점에 도달하기 전에 완료되어야 하는 정점의 개수
    visited = [False for _ in range(V)]

    for i in range(0,E*2,2):
        x,y = e_lst[i],e_lst[i+1]
        dp[x-1][y-1] = True
        cnt[y-1] += 1

    start_v = []
    for i in range(V):
        if cnt[i]==0:
            start_v.append(i)
            visited[i]=True
        
    print("#",t,sep="",end=" ")
    ans_lst = dfs(start_v)
    for i in range(V):
        ans_lst[i] += 1
    print(*ans_lst)