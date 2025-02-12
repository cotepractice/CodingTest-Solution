#SWExpertAcademy #1238 Contact

from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def dfs(current,n):
    global relations,visited

    lst = relations[current]
    for l in lst:
        if visited[l]==-1: #방문한 적 없는 경우
            visited[l]=n+1
            dfs(l,n+1)


def bfs(current,n):
    global relations,visited,max_ans,max_idx

    Q=deque()
    Q.append([current,n])
    visited[current]=True

    while Q:
        x,x_n = Q.popleft()
        if x_n > max_ans:
            max_ans = x_n
            max_idx = x
        elif x_n == max_ans:
            if x > max_idx:
                max_idx = x

        for next in relations[x]:
            if visited[next]== False:
                visited[next]=True
                Q.append([next,x_n+1])
            

T = 10

for t in range(1,T+1):
    data_l, start = map(int,input().split())
    data = list(map(int,input().split()))
    relations = [[] for _ in range(100)]
    #visited = [-1 for _ in range(100)] #dfs
    visited = [False for _ in range(100)]

    for i in range(0,data_l,2):
        relations[data[i]-1].append(data[i+1]-1)

    max_ans = -1
    max_idx = -1
    #visited[start-1] = 1
    #dfs(start-1,1)
    bfs(start-1,1)

    # for i in range(100):
    #     if visited[i] >= max_ans:
    #         max_ans=visited[i]
    #         max_idx = i
    #print("max_ans:",max_ans)
    print("#",t,sep="",end=" ")
    print(max_idx+1)
