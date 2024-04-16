# 백준 #21609 상어 중학교
# 삼성 SW 역량 테스트 기출
# 2024 상반기 삼성 신입사원 문제와 유사


#검은색 블록이 -1, 무지개 블록이 0, 일반 블록은 1~M까지
#인접한 칸은 상하좌우만

#블록그룹은 연결된 블록의 집합이며, 
#1)일반 블록이 적어도 하나 있어야하며 일반 블록의 색이 모두 같아야함
#2)검은색 블록은 속하면 안 되고 무지개 블록은 얼마나 있든 상관없음
#3)블록의 개수는 2 이상이어야함
#(?)임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해 그룹에 속한 모든 칸으로 이동할 수 있어야 함

#1. 크기가 가장 큰 블록 그룹 찾기

#2-1. 1에서 찾은 블록 그룹의 모든 블록 제거
#2-2. 블록 그룹의 수의 제곱만큼 점수 획득
#3. 격자에 중력 작용
# 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸(아래)으로 이동
#4. 격자 90도 반시계 방향으로 회전
#5. 격자에 중력

from collections import deque

#1. 크기가 가장 큰 블록 그룹 찾기.
# -1은 들어가면 안 되고 0은 가능. 일반 블록은 동일한 값이어야함
# 일반 블록 하나는 반드시 존재
def findBlock(graph,x,y):
    #print("findblock visited",visited)
    numberLst = []
    Q = deque()
    color = graph[x][y]
    zero = deque()   #graph[nx][ny]==0인경우 마지막에 visited=False로 변경
    cnt = 0 #블록 총 크기
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    Q.append((x,y))
    visited[x][y] = True    #이때 visited는 외부(main)의 visited를 가져옴
    #print("X,Y",x,y)
    while Q:
        #print("visited",visited)
        i,j = Q.popleft()
        cnt += 1
        numberLst.append((i,j))
        #print("i,j",i,j)
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            
            if 0<=nx<N and 0<=ny<N:
                #print("nx,ny",nx,ny,graph[nx][ny])
                #조건1. -1은 반드시 제거
                #조건2. 0은 반드시 포함
                #조건3. 1<=graph[nx][ny]<=M인데 color와 같지 않으면 반드시 제거 
                #조건4. graph[nx][ny] == color이면서 visited[nx][ny] == False이면 Q에 추가
                if visited[nx][ny] == True:
                    continue
                if graph[nx][ny] == -1:
                    continue
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    Q.append((nx,ny))
                    zero.append((nx,ny))
                elif 1<=graph[nx][ny]<=M:
                    if graph[nx][ny]!=color:
                        continue
                    if visited[nx][ny] == True:
                        continue
                    visited[nx][ny] = True
                    Q.append((nx,ny))
                # if 1<=vistied[nx][ny]<=M and visited[nx][ny] == True:
                #     print("1")
                #     continue
                # if graph[nx][ny] == -1:
                #     print("-1")
                #     continue
                # elif graph[nx][ny] == 0:
                #     visited[nx][ny] = True
                #     print("0")
                #     #pass
                # elif graph[nx][ny] != color:
                #     print("not color")
                #     continue
                # elif graph[nx][ny] == color:
                #     print("color")
                #     visited[nx][ny] = True  #graph[nx][ny]==0인 경우 visited 항상 False. 확실해지면 마지막에 제거
                # Q.append((nx,ny))
                #cnt += 1

    for k in range(len(zero)):
        i,j = zero.popleft()
        visited[i][j] = False

    print("FIND",x,y, cnt, numberLst)
    #print("LAST visited",visited)
    return cnt, numberLst


#입력
N, M = map(int,input().split()) #N:NxN 격자, M: 블록은 M 이하의 자연수 색

graph = [[0 for _ in range(N)] for _ in range(N)]


#Main
visited = [[False for _ in range(N)] for _ in range(N)]
maxN = 0
maxNLst = []

for i in range(N):
    graph[i] = list(map(int,input().split()))


for x in range(N):
    for y in range(N):
        if visited[x][y] == False and 1<=graph[x][y]<=M:
            #1-1. 해당 좌표에서의 dfs 실행
            #print("1 visited",visited)
            number,numberLst = findBlock(graph,x,y) #numberLst[0]은 자기자신
            #print("2 visited",visited)
            #1-2. 해당 크기가 max 크기보다 크면 업데이트
            if number > maxN:
                maxN = number
                maxNLst= numberLst
            elif number == maxN:
                #행이 가장 큰 것
                if x > maxNLst[0][0]:
                    maxN = number
                    maxNLst= numberLst
                elif x == maxNLst[0][0]:
                    #열이 가장 큰 것
                    if y > maxNLst[0][1]:
                        maxN = number
                        maxNLst= numberLst

print("maxN",maxN)
print("maxNLst",maxNLst)