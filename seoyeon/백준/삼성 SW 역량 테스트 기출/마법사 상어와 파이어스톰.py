#백준 #20058 마법사 상어와 파이어스톰
#삼성 SW 역량 테스트 기출

import copy

N, Q = map(int,input().split())
Lists = [[0 for _ in range(2**N)] for _ in range(2**N)]

for k in range(2**N):
    lists = list(map(int,input().split()))
    Lists[k] = lists

L = int(input())
L = 2**L

def split(Lists):
    #1. list에 모든 원소 저장 -> list에 행열을 list로 저장해야 할듯
    moveList = [[] for _ in range(2**(2*N)//(L**2))]
    #print(moveList)
    moveIdx = 0
    iIdx=L
    jIdx=L
    for i in range(2**N):
        moveIdx = (i//L)*4
        #print("moveIdx1",moveIdx)
        jIdx = L-1
        for j in range(2**N):
            #moveIdx += jIdx
            #print("i,j,moveIdx",i,j,moveIdx)
            moveList[moveIdx].append(Lists[i][j])
            if j==jIdx:
                jIdx += L
                moveIdx += 1
    
    #print(moveList)
    return moveList

def rotate(lst):
    #1. 이중 리스트로 변환
    doubleLst = [[-1 for _ in range(L)] for _ in range(L)]

    iIdx = 0
    cntL = L
    idx=0
    for i in range(len(lst)):
        if i==cntL:
            iIdx += 1
            idx=0
            cntL += L
        doubleLst[iIdx][idx] = lst[i]
        idx += 1
    #print(doubleLst)        

    #2. 시계 방향으로 회전
    doubleCopy = copy.deepcopy(doubleLst)

    for number in range(L):
        #print("number",number)
        changeIdx = [number,L-number-1]
        #print("changeIdx",changeIdx)
        
        for k in changeIdx:
            #print("k",k)
            if k == 0:
                for j in range(L-1):
                    #print("j+1",j+1)
                    doubleCopy[k][j+1] = doubleLst[k][j]                
                    #doubleCopy[j+1][k] = doubleLst[j][k]
            else:
                for j in range(L-1,0,-1):
                    #print("j",j)
                    doubleCopy[k][j-1] = doubleLst[k][j]
                    #doubleCopy[j-1][k] = doubleLst[j][k]
        for k in changeIdx:
            if k == 0:
                for j in range(L-1,0,-1):
                    doubleCopy[j-1][k] = doubleLst[j][k]
            else:
                for j in range(L-1):
                    doubleCopy[j+1][k] = doubleLst[j][k]    
    resultLst = []
    for i in range(L):
        for j in range(L):
            resultLst.append(doubleCopy[i][j])

    #print(doubleLst, doubleCopy)
    #print(resultLst)
    return resultLst

# def check(splitLst):
#     Lists = [[0 for _ in range(2**N)] for _ in range(2**N)]
#     #1. 하나의 list로 정리
#     idx = 0
#     #print("splitLst",splitLst)
#     iStart = 0
#     iEnd = (2**N)//L
#     #print(N,L,iEnd)
#     jStart = 0
#     jEnd = L

#     for i in range(iStart,iEnd):
#         for j in range(jStart,jEnd):
#             Lists[idx].append(splitLst[i][j])
#         idx += 1
#         jStart = jEnd
#         jEnd += L

    # #while True:
    # for i in range(len(splitLst)):
    #     while True:
    #         for j in range(jStart,jEnd):
    #             if jEnd > L**2:
    #                 break
    #             Lists[idx].append(splitLst[i][j])
    #         jEnd += L
    #         # if jEnd >= len(splitLst[0]):
    #         #     break
    #     idx += 1
            
    print(Lists)


#1. 부분 격자 나누기
splitLst = split(Lists)
#2. 부분 격자 시계 방향으로 90도 회전
print("splitLst1",splitLst)
if L!=1:
    for idx in range(len(splitLst)):
        splitLst[idx] = rotate(splitLst[idx])
print("splitLst2",splitLst)

#3. 인접한 칸 확인
Lists = check(splitLst)