#SWExpertAcademy #3124 최소 스패닝 트리
#Kruskal's algorithm

#루트 노드 탐색
def find_parent(parent,n):
    if parent[n]!=n:
        parent[n] = find_parent(parent,parent[n])
    return parent[n]

#두 정점의 집합 합치기
def union(parent,a,b):
    #각각의 루트 노드 탐색
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    #둘 중 작은 정점으로 루트 노드 변경
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for t in range(1,T+1):
    V, E = map(int,input().split())
    edges = [[] for _ in range(E)] 
    parent = [i for i in range(V)] #대표 정점. 루트 노드
    result = 0

    for e in range(E):
        a,b,c = map(int,input().split())
        edges[e] = [c,a-1,b-1]

    #가중치 오름차순으로 정렬
    edges.sort()

    for edge in edges:
        c,a,b = edge

        #사이클 없는 경우
        if find_parent(parent,a) != find_parent(parent,b):
            union(parent,a,b)
            result += c

    print("#",t,sep="",end=" ")
    print(result)
    