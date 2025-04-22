#BFS
from collections import deque
def solution(n, edge):
    answer = 0
    
    edge_n = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    for e in edge:
        x,y = e
        edge_n[x].append(y)
        edge_n[y].append(x)
    
    Q = deque()
    Q.append([0,1]) #[간선길이,노드]
    visited[1]=True
    max_len = 0
    while Q:
        len, node = Q.popleft()
        if len>=max_len:
            if len==max_len:
                answer += 1
            else:
                max_len = len
                answer = 1
        for next in edge_n[node]:
            if visited[next]==False:
                visited[next]=True
                Q.append([len+1,next])
    
    return answer