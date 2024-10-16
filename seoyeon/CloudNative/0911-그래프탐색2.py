from collections import deque

N, M = map(int,input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
	graph[i] = list(input())


d = [[0,1],[0,-1],[1,0],[-1,0]]
									
def bfs(x,y):
	Q = deque()
	Q.append([x,y])
	visited[x][y] = True
	size = 0
	
	while Q:
		size += 1
		nx, ny = Q.popleft()
		#print("size",size,"x,y",nx,ny)
		for i in range(4):
			mx = nx+d[i][0]
			my = ny+d[i][1]

			if 0<=mx<M and 0<=my<N:
				if visited[mx][my]==False and graph[mx][my]=="#":
					visited[mx][my] = True
					Q.append([mx,my])
					
	return size

cnt = 0
max_size = 0

visited = [[False for _ in range(N)] for _ in range(M)]
									
for i in range(M):
	for j in range(N):
		if graph[i][j] == "#" and visited[i][j]==False:
			cnt += 1
			size=bfs(i,j)
			if size>max_size:
				max_size = size
				
									
print(cnt)
print(max_size)