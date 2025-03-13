from collections import deque
import copy

cp_graph = []
cp_visited = []

def bfs(depth,index):
    global cp_graph, cp_visited
    #print("cp_graph:",cp_graph)
    #print("cp_visited:",cp_visited)
    lst = cp_graph[index]
    Q = deque()
    for l in range(len(lst)):
        Q.append(lst[l])
        cp_visited[lst[l]]=True
    
    cnt = 0
    while Q:
        idx = Q.popleft()
        cnt += 1
        
        for l in cp_graph[idx]:
            if cp_visited[l]==False:
                cp_visited[l]=True
                Q.append(l)

    return cnt

def solution(n, wires):
    global cp_visited, cp_graph
    answer = float("inf")
    
    connect_graph = [[] for _ in range(n+1)] #connect_graph[i]=[j,l,...]: i와 연결된 송전탑 인덱스 리스트
    visited = [False for _ in range(n+1)]
    
    for wire in wires:
        x,y = wire
        connect_graph[x].append(y)
        connect_graph[y].append(x)
    
    for wire in wires:
        cp_visited = [False for _ in range(n+1)]
        cp_graph = copy.deepcopy(connect_graph)
        x,y = wire
        cp_graph[x].remove(y)
        cp_graph[y].remove(x)
        
        result = [-1 for _ in range(2)]
        cnt = 0
        for i in range(1,n+1):
            if cp_visited[i]==False:
                cp_visited[i]=True
                result[cnt]=bfs(1,i)
                cnt += 1
        
        answer = min(answer, abs(result[0]-result[1]))
    return answer