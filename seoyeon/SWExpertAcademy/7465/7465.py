#SWExpertAcademy 7465 창용 마을 무리의 개수

def dfs(i):
    global relations,visited,ans

    lst = relations[i]
    for l in lst:
        if visited[l]==False:
            visited[l]=True
            dfs(l)

T = int(input())

for t in range(1,T+1): 
    N,M = map(int,input().split())
    relations = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    ans = 0

    for m in range(M):
        x,y = map(int,input().split())

        relations[x-1].append(y-1)
        relations[y-1].append(x-1)
    
    for i in range(N):
        if visited[i]==False:
            ans += 1
            dfs(i)
    print("#",t,sep="",end=" ")
    print(ans)