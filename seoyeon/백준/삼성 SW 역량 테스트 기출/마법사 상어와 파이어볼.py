#백준 #20056 마법사 상어와 파이어볼
#삼성 SW 역량 테스트 기출

N, M, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(N)]    #파이어볼 개수
fireballs = [(0,0,0,0,0) for _ in range(M)] #(x,y,질량,속력,방향)

for k in range(M):
    r,c,m,s,d = map(int, input().split())
    fireballs[k] = (r-1,c-1,m,s,d)
    maps[r-1][c-1] += 1

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    #print("fireballs",fireballs)
    #1. 모든 파이어볼이 자신의 방향과 속력대로 이동
    newFireballs = []   #이동한 파이어볼 정보
    for k in range(len(fireballs)):
        r,c,m,s,d = fireballs[k]
        x = (r + s*dx[d]) % N   #격자가 붙어있기때문
        y = (c + s*dy[d]) % N
        maps[r][c] -= 1 #기존 위치에서 파이어볼 제거
        maps[x][y] += 1 #이동한 위치에 파이어볼 추가
        newFireballs.append((x,y,m,s,d))
    #print("newFireballs",newFireballs)

    separateFireballs = []  #결과적으로 아래 명령 이후에 존재하는 파이어볼
    #2이상의 경우    
    for i in range(N):
        for j in range(N):
            #print("i,j,n",i,j,N)
            if maps[i][j] >= 2:
                #2. 2 이상의 파이어볼이 있는 위치 처리
                #a. 같은 칸의 파이어볼 합치기
                #print("here",i,j)
                newM = 0
                newS = 0
                newD = (0,2,4,6)
                Dlst = []
                cnt = 0
                maps[i][j] = 1
                #b. 파이어볼이 4개의 파이어볼의 질량,속력,방향 계산
                for k in range(len(newFireballs)):
                    if newFireballs[k][0] == i and newFireballs[k][1] == j:
                        newM += newFireballs[k][2]
                        newS += newFireballs[k][3]
                        Dlst.append(newFireballs[k][4])
                        cnt += 1
                newM = newM//5
                if newM == 0:  #질량이 0이면 소멸
                    continue
                newS = newS//cnt
                #print("new",newM,newS)
                check = 0
                for l in range(cnt):
                    if l == 0:
                        check = Dlst[l]
                    else:
                        if check%2 != Dlst[l]%2:
                            newD = (1,3,5,7)
                            break
                #print("new",newD)
                for p in range(4):
                    separateFireballs.append((i,j,newM,newS,newD[p]))
            else:
                for k in range(len(newFireballs)):
                    #print(i,j,k,newFireballs[k],newFireballs[k][0]==i,newFireballs[k][1]==j)
                    if (newFireballs[k][0] == i and newFireballs[k][1] == j):
                        separateFireballs.append((i,j,newFireballs[k][2],newFireballs[k][3],newFireballs[k][4]))

    #print("separateFireballs",separateFireballs)
    fireballs = separateFireballs 

#print(separateFireballs)
result = 0
for k in range(len(separateFireballs)):
    result += separateFireballs[k][2]
print(result)