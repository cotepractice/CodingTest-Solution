# 포탑 부수기

from collections import deque

N, M, K = map(int,input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph[i]=list(map(int,input().split()))


#공격자 선정
def getAttacker(graph):
    answers = (0,0)
    low = 5001
    #1.공격력이 가장 낮은 포탑 선택
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:    #0인 경우 포탑이 부서짐을 의미
                continue
            #기준1
            if graph[i][j] < low:
                low = graph[i][j]
                low_x,low_y = i,j
            elif graph[i][j] == low:
                #기준2
                if history[i][j] > history[low_x][low_y]:   #수가 큰 것이 최근
                    low_x,low_y = i,j
                elif history[i][j] == history[low_x][low_y]:
                    #기준3
                    if i+j > low_x+low_y:
                        low_x,low_y = i,j
                    elif i+j == low_x+low_y:
                        #기준4
                        if j > low_y:
                            low_x,low_y = i,j
    answers = (low_x,low_y)
    return answers

#공격자 공격1: 가장 강한 포탑 선택
def getTarget(graph,x,y):
    answers = (0,0)
    high = -1

    for i in range(N):
        for j in range(M):
            #0인 경우 제외
            if graph[i][j] == 0:
                continue
            #공격자 제외
            if x==i and y==j:
                continue
            #기준1
            if graph[i][j] > high:
                high = graph[i][j]
                high_x,high_y = i,j
            elif graph[i][j] == high:
                #기준2
                if history[i][j] < history[high_x][high_y]:
                    high_x,high_y = i,j
                elif history[i][j] == history[high_x][high_y]:
                    #기준3
                    if i+j < high_x+high_y:
                        high_x,high_y = i,j
                    elif i+j == high_x+high_y:
                        #기준4
                        if y < high_y:
                            high_x,high_y = i,j
    answers = (high_x,high_y)
    return answers

#레이저 공격
def attackLaser(graph,x1,y1,x2,y2): #x1,y1은 공격자의 위치, x2,y2는 공격받는 포탑 위치
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    attackN = graph[x1][y1]
    global routeLst
    #최단 경로 존재하는지 확인
    visited = [[False for _ in range(M)] for _ in range(N)]
    Q = deque()
    Q.append((x1,y1,[]))    #x,y,route
    visited[x1][y1] = True

    while Q:
        x,y,route = Q.popleft()
        for dx,dy in d:
            nx = (x+dx)%4
            ny = (y+dy)%4

            if visited[nx][ny]==True:
                continue
            if graph[nx][ny]==0:
                continue

            #target에 도달한 경우
            if nx==x2 and ny==y2:
                graph[nx][ny] -= attackN
                for rx,ry in route:
                    graph[rx][ry] -= attackN//2
                routeLst = route
                return True
            
            #target은 아닌 이동 경로의 경우
            tmp_route = route[:]
            tmp_route.append((nx,ny))
            visited[nx][ny] = True
            Q.append((nx,ny,tmp_route))

    return False


#포탄 공격
def attackBomb(graph,x1,y1,x2,y2):

    attackN = graph[x1][y1]

    #공격 대상은 attackN만큼 피해
    graph[x2][y2] -= attackN
    #공격 대상 주위는 attackN//2만큼 피해
    d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for k in range(8):
        nx = x2+d[k][0]
        ny = y2+d[k][1]
        if not 0<=nx<4:
            if nx<0:
                nx += 4
            elif nx>=4:
                nx -= 4
        if not 0<=ny<4:
            if ny<0:
                ny += 4
            elif ny>=4:
                ny -= 4
        graph[nx][ny] -= attackN//2

#포탑 부서짐&정비
def maintenance(graph,x1,y1,x2,y2,routeLst):
    for i in range(N):
        for j in range(M):
            if graph[i][j] <= 0:
                graph[i][j] = 0
            else:
                #print("i,j",i,j,"x1,y1",x1,y1,"bool",i!=x1 and j!=y1)
                if (i==x1 and j==y1) or (i==x2 and j==y2):
                    continue
                if (i,j) in routeLst:
                    continue
                graph[i][j] += 1

history = [[0 for _ in range(M)] for _ in range(N)]   #공격 포탑에 현재 시간 기록

#Main

for k in range(K):  #k는 history 기록을 위한 변수
    x,y = getAttacker(graph)
    #print(graph)
    graph[x][y] += N+M
    target_x,target_y,val = getTarget(graph,x,y)
    #print(graph)
    if not attackLaser(graph,x,y,target_x,target_y):
        attackBomb(graph,x,y,target_x,target_y)
    #print(graph)
    #print("routeLst",routeLst)
    history[x][y] = k
    maintenance(graph,x,y,target_x,target_y,routeLst)
    #print(graph)

#가장 강한 포탑
max = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]>max:
            max = graph[i][j]

print(max)