def find_route(x, arr, endpoint, route, visited):  # 집에서 회사 (S -> T)

    if x == endpoint:
        for i in arr:
            route.add(i)
        return
    for v in graph[x]:
        if v in route:  # x에서 v로 가는 경로가 존재하는데, v가 S->T로 갈 수 있는 경로에 이미 포함되어 있다면, 더 확인할 필요 없이 x도 그 경로에 포함시켜준다.
            route.add(x)
            visited[(x, v)] = 1
            continue
        if visited.get((x, v)) == None:
            visited[(x, v)] = 1
            arr.append(v)
            find_route(v, arr, endpoint, route, visited)
            arr.pop()


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

S, T = map(int, input().split())  # 집, 회사
visited_go = dict()
visited_back = dict()
go_route = set()  # 출근길에 들른 동네 정보
back_route = set()  # 퇴근길에 들른 동네 정보

find_route(S, [S], T, go_route, visited_go)
find_route(T, [T], S, back_route, visited_back)

intersection = go_route & back_route
print(len(intersection) - 2)


