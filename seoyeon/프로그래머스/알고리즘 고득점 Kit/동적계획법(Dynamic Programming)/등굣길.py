#프로그래머스 알고리즘 고득점 Kit 
#동적계획법
#등굣길

#1st
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    regions = [[0 for _ in range(m)] for _ in range(n)]
    
    #1. 물에 잠긴 위치 파악
    for i in range(n):
        for j in range(m):
            lst = [i, j]
            if (lst in puddles):
                regions[i-1][j-1] = 10000   #m,n이 100이하의 자연수이므로 그 수보다 크도록 설정
                
    #2. dp 사용해 현재 위치(i,j)까지의 최단거리 계산
    for i in range(n):
        for j in range(m):
            if (i==0 and j==0): #처음 시작
                continue
            if (regions[i][j] == 10000):   #물이 잠긴 경우 처리 x
                continue
            if (i==0):
                regions[i][j] = regions[i][j-1]+1
            elif (j==0):
                regions[i][j] = regions[i-1][j]+1
            else:
                regions[i][j] = min(regions[i][j-1]+1, regions[i-1][j]+1)
        
    answer = (regions[n-1][m-1]-1) % 1000000007    #마지막 한 번은 카운팅하지 않음
    return answer

#2nd: 정확성 30/100 효율성 0/100
def solution(m, n, puddles):
    puddles = [[q-1,p-1] for [p,q] in puddles]
    regions = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            #(0,0)과 (0,?), (?,0) 초기화
            if (i==0 and j==0): 
                continue
            if (i==0 or j==0):
                regions[i][j] = 1
            else:
                            
                #물에 잠긴 경우 처리 x
                lst = [i,j]
                if (lst in puddles):   
                    continue
                
                regions[i][j] = (regions[i-1][j] + regions[i][j-1])
            
    return regions[n-1][m-1]

#3rd: 정확도 100/100 효율성 100/100
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    regions = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            #(0,0)과 (0,?), (?,0) 초기화
            if (i==1 and j==1): 
                regions[i][j] = 1
                continue
                            
            #물에 잠긴 경우 처리 x
            if ([i,j] in puddles):   
                continue
            
            regions[i][j] = regions[i-1][j] + regions[i][j-1]
    
    answer = regions[n][m] % 1000000007        
    return answer