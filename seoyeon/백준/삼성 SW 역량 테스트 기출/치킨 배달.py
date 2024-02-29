#백준 #15686 치킨 배달
#삼성 SW 역량 테스트 기출

N, M = map(int, input().split())
Maps = [[0 for _ in range(N)] for _ in range(N)]
chickens = []   #치킨 좌표
houses = []     #집 좌표


for i in range(N):
    Maps[i] = list(map(int, input().split()))

chickenCnt = 0
houseCnt = 0
for i in range(N):
    for j in range(N):
        if Maps[i][j] == 2:
            chickens.append((i,j))
            chickenCnt += 1            
        elif Maps[i][j] == 1:
            houses.append((i,j))
            houseCnt += 1

allD = [[0 for _ in range(chickenCnt)] for _ in range(houseCnt)]    #집과 치킨집의 모든 거리
dp = [0 for _ in range(chickenCnt)] #치킨거리에 해당하는 치킨집 카운트 => 많을 수록 M개에 들어갈 확률 높음

for i in range(houseCnt):
    hx, hy = houses[i]
    min = 2*N   #치킨거리 
    idx = []    #치킨거리에 해당하는 인덱스
    for j in range(chickenCnt):
        cx, cy = chickens[j]
        absN = abs(hx-cx) + abs(hy-cy)
        allD[i][j] = absN

        if absN<min:
            min = absN
            idx = [j]
        elif absN==min:
            idx.append(j)
    for k in range(len(idx)):
        index = idx[k]
        dp[index] += 1

# print("chicken",chickens)
# print("house",houses)
# print("allD",allD)
# print("dp",*dp)

#M개 선택 => 겹치는 경우 생각 X
chooseM = [(0,0) for _ in range(chickenCnt)]
for i in range(chickenCnt):
    chooseM[i] = (dp[i],i)
chooseM.sort(reverse=True)  #많은 순서로 정렬
#print("chooseM",chooseM)

#겹치는 횟수 없는 경우로 가정하고 진행
index = [0 for _ in range(M)]
for i in range(M):
    index[i] = chooseM[i][1]
# print("index",index)

#선택한 M개의 치킨집 중에서 치킨 거리 계산
result = 0
for k in range(houseCnt):
    d = 2*N
    for i in index:
        if allD[k][i] < d:
            d = allD[k][i]
    result += d
print(result)