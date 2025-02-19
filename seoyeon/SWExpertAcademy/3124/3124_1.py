#SWExpertAcademy #3124 최소 스패닝 트리
#Prim's Algorithm
import heapq

def prim(n):
    
    visited=[False for _ in range(V)] 
    weights=[float("inf") for _ in range(V)] #weight[0] 노드 0으로 갈 수 있는 최소 가중치 값

    weights[n]=0
    heap_edge = [[0,n]] #[가중치,노드]
    heapq.heapify(heap_edge)

    while heap_edge:
        weight,node = heapq.heappop(heap_edge)
        
        if visited[node]==False:
            visited[node]=True

            for edge in edges[node]:
                next_w, next_n = edge
                if visited[next_n]==False and next_w<weights[next_n]:
                    weights[next_n]=next_w
                    heapq.heappush(heap_edge,[next_w,next_n])

    return sum(weights)

T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())
    edges = [[] for _ in range(V)]

    for e in range(E):
        a,b,c = map(int,input().split())
        edges[a-1].append([c,b-1])
        edges[b-1].append([c,a-1])

    ans = prim(0)
    print("#",t,sep="",end=" ")
    print(ans)