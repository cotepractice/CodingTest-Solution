#SWExpert Academy #1247 최적경로
#TSP

def dfs(index,last_x,last_y,d):
    global ans

    #모든 경로 탐색 완료
    if d>=ans:
        return
    #모든 경로 탐색 완료한 경우
    if index==N:
        d += abs(last_x-house[0]) + abs(last_y-house[1])
        ans = min(ans,d)
        return

    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            temp = d + abs(last_x-customer[i][0]) + abs(last_y-customer[i][1])
            dfs(index+1,customer[i][0],customer[i][1],temp)
            visited[i]=False


T = int(input())

for t in range(1,T+1):
    N = int(input())

    lst = list(map(int,input().split())) #회사, 집, N명의 고객의 좌표
    matrix = [[0 for _ in range(100)] for _ in range(100)] #1:회사,2:집,3:고객집
    visited = [False for _ in range(N)]

    #회사 -> 고객 -> 집
    #거리는 |x1-x2|+|y1-y2|
    company = [lst[0]-1, lst[1]-1]
    house = [lst[2]-1,lst[3]-1]
    customer = [[lst[i]-1,lst[i+1]-1] for i in range(4,N*2+4,2)]

    matrix[company[0]][company[1]] = 1
    matrix[house[0]][house[1]] = 2
    for i in range(N):
        matrix[customer[i][0]][customer[i][1]] = 3

    ans = float("inf")
    dfs(0,company[0],company[1],0)
    print("#",t,sep="",end=" ")
    print(ans)