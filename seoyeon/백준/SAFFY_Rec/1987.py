#백준 #1987 알파벳

def dfs(x,y,alpha,cnt):
    global ans

    if cnt>ans:
        ans = cnt

    d_lst = [[0,-1],[0,1],[1,0],[-1,0]]

    for dx,dy in d_lst:
        nx = x+dx
        ny = y+dy
        if 0<=nx<R and 0<=ny<C and visited[nx][ny]==False and boards[nx][ny] not in alpha:
            visited[nx][ny]=True
            alpha[boards[nx][ny]]=0
            dfs(nx,ny,alpha,cnt+1)
            visited[nx][ny]=False
            del alpha[boards[nx][ny]]
            


R, C = map(int,input().split())
boards = ["" for _ in range(R)]

for r in range(R):
    lst = input()
    boards[r] = lst

ans = 0
visited=[[False for _ in range(C)] for _ in range(R)]

visited[0][0]=True
dict = {}
dict[boards[0][0]]=0
dfs(0,0,dict,1)

print(ans)