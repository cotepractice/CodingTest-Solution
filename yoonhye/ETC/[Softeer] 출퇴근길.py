def DFS(start, visit, adj):
    stack = [start]
    while stack:
        now = stack.pop()
        if visit[now] == 1:
            continue
        visit[now] = 1
        for neighbor in adj[now]:
            stack.append(neighbor)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
adjR = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adjR[b].append(a)
S, T = map(int, input().split())

fromS = [0] * (n + 1)
fromS[T] = 1
DFS(S, fromS, adj)

fromT = [0] * (n + 1)
fromT[S] = 1
DFS(T, fromT, adj)

toS = [0] * (n + 1)
DFS(T, toS, adjR)

toT = [0] * (n + 1)
DFS(S, toT, adjR)

count = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1

print(count - 2)
