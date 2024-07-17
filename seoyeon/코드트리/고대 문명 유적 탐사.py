#1. 테스트케이스 2에서 틀렸습니다 < rotate() 함수 수정해 해결
import copy
from collections import deque

def bfs(x,y,k,visited,maps):
    n = 0
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    lst = [[x,y]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:
        x1, y1 = Q.popleft()
        n += 1
        for d in range(4):
            nx = x1+dx[d]
            ny = y1+dy[d]

            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                if maps[nx][ny] == k:
                    lst.append([nx,ny])
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
    
    if n>=3:
        return n, visited, lst
    else:
        return 0, visited, []


def findFirstVal(maps):
    sum = 0
    sum_k = 0
    empty_lst = []
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for k in range(1,8):
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 0:
                    sum_k, visited, lst = bfs(i,j,maps[i][j],visited,maps)
                    if lst!=[]:
                        empty_lst.append(lst)
                    sum += sum_k   

    return sum,empty_lst

#입력: 좌표 x,y
#출력: 유물 1차 가치, 새로운 graph
def rotate():
    first_sum = 0
    lst = []
    maps_result = []
    sum_rotate_n = 0
    for i in range(1,4):
        for j in range(1,4):
            sum90,lst90,maps90 = rotate90(i,j)
            sum180,lst180,maps180 = rotate180(i,j)
            sum270,lst270,maps270 = rotate270(i,j)
            if sum90 >= first_sum:      
                first_sum = sum90
                lst = lst90
                maps_result = maps90
                sum_rotate_n = 90
            if first_sum <= sum180 and sum90 < sum180:
                if first_sum == sum180 and sum_rotate_n == 90:
                    continue
                first_sum = sum180
                lst = lst180
                maps_result = maps180
                sum_rotate_n = 180
            if first_sum < sum270 and sum90 < sum270 and sum180 <sum270:
                first_sum = sum270
                lst = lst270
                maps_result = maps270
                sum_rotate_n = 270

    return first_sum,lst, maps_result


def rotate90(x,y):
    maps_copy = copy.deepcopy(maps)

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue

            if i==x-1:
                maps_copy[j][y+1] = maps[i][j]
            elif i==x:
                maps_copy[j][y] = maps[i][j]
            elif i==x+1:
                maps_copy[j][y-1] = maps[i][j]
    
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate180(x,y):
    maps_copy = copy.deepcopy(maps)

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x][y+1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]

    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate270(x,y):
    maps_copy = copy.deepcopy(maps)
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x+1][y] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]
            elif i==x+1: 
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy


def full_lst(lst,maps,full_idx):
    sorted_lst = []
    for k in range(len(lst)):
        for l in range(len(lst[k])):
            sorted_lst.append(lst[k][l])

    sorted_lst.sort(key=lambda x:[x[1],-x[0]])
    
    for m in range(len(sorted_lst)):
        maps[sorted_lst[m][0]][sorted_lst[m][1]] = M_lst[full_idx]
        full_idx += 1

    return maps, full_idx


#main
K, M = map(int,input().split())
maps = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    maps[i] = list(map(int,input().split()))
M_lst = list(map(int,input().split()))

answer_lst = []
full_idx = 0

for k in range(K):
    answer = 0
    #1. 회전
    sum,lst,maps_result = rotate()

    maps = maps_result
    
    #2. 유적 탐사
    while True:
        if full_idx == M:
            answer = 0
            break
        chain_sum, chain_empty_lst = findFirstVal(maps)
        
        if chain_sum==0:
            break
        answer += chain_sum

        maps, full_idx = full_lst(chain_empty_lst,maps,full_idx)
    
    if answer != 0:
        answer_lst.append(answer)

print(*answer_lst)


#2. 테스트케이스 3 틀렸습니다 
#테스트케이스 2에서 틀림
import copy
from collections import deque

def bfs(x,y,k,visited,maps):
    n = 0
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    lst = [[x,y]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:
        x1, y1 = Q.popleft()
        n += 1
        for d in range(4):
            nx = x1+dx[d]
            ny = y1+dy[d]

            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                if maps[nx][ny] == k:
                    lst.append([nx,ny])
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
    
    if n>=3:
        return n, visited, lst
    else:
        return 0, visited, []


def findFirstVal(maps):
    sum = 0
    sum_k = 0
    empty_lst = []
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for k in range(1,8):
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 0:
                    sum_k, visited, lst = bfs(i,j,maps[i][j],visited,maps)
                    if lst!=[]:
                        empty_lst.append(lst)
                    sum += sum_k   

    return sum,empty_lst

#입력: 좌표 x,y
#출력: 유물 1차 가치, 새로운 graph
def rotate():
    first_sum = 0
    lst = []
    maps_result = []
    sum_rotate_n = 0
    for i in range(1,4):
        for j in range(1,4):
            sum90,lst90,maps90 = rotate90(i,j)
            sum180,lst180,maps180 = rotate180(i,j)
            sum270,lst270,maps270 = rotate270(i,j)
            # if sum90==sum180==sum270==0:
            #     return 0,[],maps

            if sum90 >= first_sum and sum_rotate_n != 90:  
                #print("1",i,j,sum90)    
                first_sum = sum90
                lst = lst90
                maps_result = maps90
                sum_rotate_n = 90
            if first_sum <= sum180 and sum90 < sum180:
                if first_sum == sum180 and sum_rotate_n == 90:
                    continue
                #print("2",i,j,sum180)
                first_sum = sum180
                lst = lst180
                maps_result = maps180
                sum_rotate_n = 180
            if first_sum < sum270 and sum90 < sum270 and sum180 <sum270:
                #print("3",i,j,sum270)
                first_sum = sum270
                lst = lst270
                maps_result = maps270
                sum_rotate_n = 270

    if first_sum == 0:
        return 0,[],maps
    else:
        return first_sum,lst, maps_result


def rotate90(x,y):
    maps_copy = copy.deepcopy(maps)
    #print("90")

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue

            if i==x-1:
                maps_copy[j][y+1] = maps[i][j]
            elif i==x:
                maps_copy[j][y] = maps[i][j]
            elif i==x+1:
                maps_copy[j][y-1] = maps[i][j]
    
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate180(x,y):
    #print("180")
    maps_copy = copy.deepcopy(maps)

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x][y+1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]

    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate270(x,y):
    #print("270")
    maps_copy = copy.deepcopy(maps)
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x+1][y] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]
            elif i==x+1: 
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy


def full_lst(lst,maps,full_idx):
    sorted_lst = []
    for k in range(len(lst)):
        for l in range(len(lst[k])):
            sorted_lst.append(lst[k][l])

    sorted_lst.sort(key=lambda x:[x[1],-x[0]])
    
    for m in range(len(sorted_lst)):
        maps[sorted_lst[m][0]][sorted_lst[m][1]] = M_lst[full_idx]
        full_idx += 1

    return maps, full_idx


#main
K, M = map(int,input().split())
maps = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    maps[i] = list(map(int,input().split()))
M_lst = list(map(int,input().split()))

answer_lst = []
full_idx = 0

for k in range(K):
    answer = 0
    #1. 회전
    sum,lst,maps_result = rotate()
    if sum==0:
        #print("here")
        break

    maps = maps_result
    #print("maps1",maps)
    
    #2. 유적 탐사
    while True:
        chain_sum, chain_empty_lst = findFirstVal(maps)
        
        if chain_sum==0:
            break
        answer += chain_sum

        maps, full_idx = full_lst(chain_empty_lst,maps,full_idx)
        #print("maps2",maps)
    
    if answer != 0:
        answer_lst.append(answer)

print(*answer_lst)

#3. 테스트케이스4에서 틀렸습니다

import copy
from collections import deque

def bfs(x,y,k,visited,maps):
    n = 0
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    lst = [[x,y]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:
        x1, y1 = Q.popleft()
        n += 1
        for d in range(4):
            nx = x1+dx[d]
            ny = y1+dy[d]

            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                if maps[nx][ny] == k:
                    #print("nxny",nx,ny,"n",n,"k",k)
                    lst.append([nx,ny])
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
    
    if n>=3:
        return n, visited, lst
    else:
        return 0, visited, []


def findFirstVal(maps):
    sum = 0
    sum_k = 0
    empty_lst = []
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for k in range(1,8):
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 0:
                    sum_k, visited, lst = bfs(i,j,maps[i][j],visited,maps)
                    if lst!=[]:
                        empty_lst.append(lst)
                    sum += sum_k   

    return sum,empty_lst

#입력: 좌표 x,y
#출력: 유물 1차 가치, 새로운 graph
def rotate():
    first_sum = 0
    lst = []
    maps_result = []
    sum_rotate_n = 0
    pos = [float("inf"),float("inf")]
    for i in range(1,4):
        for j in range(1,4):
            sum90,lst90,maps90 = rotate90(i,j)
            sum180,lst180,maps180 = rotate180(i,j)
            sum270,lst270,maps270 = rotate270(i,j)
            #print("sums",sum90,sum180,sum270)

            #90도 회전
            if sum90 >= first_sum:
                if sum90 == first_sum and sum_rotate_n == 90:
                    if pos[1]<j:
                        continue
                    elif pos[1]==j and pos[0]<i:
                        continue
                
                first_sum = sum90
                lst = lst90
                maps_result = maps90
                sum_rotate_n = 90
                pos = [i,j]
                                          
            #180도 회전
            if sum180 >= first_sum:
                if sum180 == first_sum and sum_rotate_n == 90:
                    continue
                if sum180 == first_sum and sum_rotate_n==180:
                    if pos[1]<j:
                        continue
                    elif pos[1]==j and pos[0]<i:
                        continue
                first_sum = sum180
                lst = lst180
                maps_result = maps180
                sum_rotate_n = 180
                pos = [i,j]                        
            
            #270도 회전
            if sum270 >= first_sum:
                if sum270==first_sum and (sum_rotate_n ==90 or sum_rotate_n==180):
                    continue
                elif sum270==first_sum and sum_rotate_n==270:
                    if pos[1]<j:
                        continue
                    elif pos[1]==j and pos[0]<i:
                        continue
                first_sum = sum270
                lst = lst270
                maps_result = maps270
                sum_rotate_n = 270    
                pos = [i,j]               
    
    #print("pos",pos, sum_rotate_n,first_sum)
    if first_sum == 0:
        return 0,[],maps
    else:
        return first_sum,lst, maps_result


def rotate90(x,y):
    maps_copy = copy.deepcopy(maps)
    #print("maps1",maps_copy)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue

            if i==x-1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x-1][y] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
    
    sum,lst = findFirstVal(maps_copy)
    #print("maps2",maps_copy)
    return sum,lst,maps_copy

def rotate180(x,y):
    #print("180")
    maps_copy = copy.deepcopy(maps)

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x][y+1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]

    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate270(x,y):
    #print("270")
    maps_copy = copy.deepcopy(maps)
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x+1][y] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]
            elif i==x+1: 
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy


def full_lst(lst,maps,full_idx):
    sorted_lst = []
    for k in range(len(lst)):
        for l in range(len(lst[k])):
            sorted_lst.append(lst[k][l])

    sorted_lst.sort(key=lambda x:[x[1],-x[0]])
    
    for m in range(len(sorted_lst)):
        maps[sorted_lst[m][0]][sorted_lst[m][1]] = M_lst[full_idx]
        full_idx += 1

    return maps, full_idx


#main
K, M = map(int,input().split())
maps = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    maps[i] = list(map(int,input().split()))

M_lst = list(map(int,input().split()))

answer_lst = []
full_idx = 0

# maps = [[7, 5, 4, 2, 7], [5, 6, 7, 6, 1], [1, 3, 1, 5, 4], [7, 2, 5, 7, 1], [5, 4, 3, 2, 7]]
# print("RESULT:",rotate90(2,1))

for k in range(K):
    answer = 0
    #1. 회전
    sum,lst,maps_result = rotate()
    if sum==0:
        #print("here")
        break

    maps = maps_result
    #print("maps1",maps)
    
    #2. 유적 탐사
    while True:
        chain_sum, chain_empty_lst = findFirstVal(maps)
        
        if chain_sum==0:
            break
        answer += chain_sum

        maps, full_idx = full_lst(chain_empty_lst,maps,full_idx)
        #print("maps2",maps)
    
    if answer != 0:
        answer_lst.append(answer)
    #print("answer",answer)

print(*answer_lst)

#4. 테스트케이스 4에서 틀렸습니다
#rotate 코드 수정
import copy
from collections import deque

def bfs(x,y,k,visited,maps):
    n = 0
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    lst = [[x,y]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:
        x1, y1 = Q.popleft()
        n += 1
        for d in range(4):
            nx = x1+dx[d]
            ny = y1+dy[d]

            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                if maps[nx][ny] == k:
                    #print("nxny",nx,ny,"n",n,"k",k)
                    lst.append([nx,ny])
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
    
    if n>=3:
        return n, visited, lst
    else:
        return 0, visited, []


def findFirstVal(maps):
    sum = 0
    sum_k = 0
    empty_lst = []
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for k in range(1,8):
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 0:
                    sum_k, visited, lst = bfs(i,j,maps[i][j],visited,maps)
                    if lst!=[]:
                        empty_lst.append(lst)
                    sum += sum_k   

    return sum,empty_lst

#입력: 좌표 x,y
#출력: 유물 1차 가치, 새로운 graph
def rotate():
    first_sum = 0
    lst = []
    maps_result = []
    sum_rotate_n = 0
    pos = [float("inf"),float("inf")]
    for i in range(1,4):
        for j in range(1,4):
            sum90,lst90,maps90 = rotate90(i,j)
            sum180,lst180,maps180 = rotate180(i,j)
            sum270,lst270,maps270 = rotate270(i,j)
            #print(i,j,"sum!",sum90,sum180,sum270,"FIRST_SUM",first_sum)
            #90도 회전
            if sum90 >= first_sum:
                if sum90>first_sum:
                    first_sum = sum90
                    lst = lst90
                    maps_result = maps90
                    sum_rotate_n = 90
                    pos = [i,j]
                else:
                    if sum_rotate_n != 90:
                        first_sum = sum90
                        lst = lst90
                        maps_result = maps90
                        sum_rotate_n = 90
                        pos = [i,j]
                    else:
                        if (sum_rotate_n==90 and pos[1]>j) or (sum_rotate_n==90 and pos[1]==j and pos[0]>i):
                            first_sum = sum90
                            lst = lst90
                            maps_result = maps90
                            sum_rotate_n = 90
                            pos = [i,j]
                                          
            #180도 회전
            if sum180 >= first_sum:
                if sum180>first_sum:
                    first_sum = sum180
                    lst = lst180
                    maps_result = maps180
                    sum_rotate_n = 180
                    pos = [i,j]   
                else:
                    if sum_rotate_n!=90:
                        first_sum = sum180
                        lst = lst180
                        maps_result = maps180
                        sum_rotate_n = 180
                        pos = [i,j]   
                    elif (sum_rotate_n==180 and pos[1]>j) or (sum_rotate_n==180 and pos[1]==j and pos[0]>i):
                        first_sum = sum180
                        lst = lst180
                        maps_result = maps180
                        sum_rotate_n = 180
                        pos = [i,j]                        
            
            #270도 회전
            if sum270 >= first_sum:
                if sum270==first_sum:
                    first_sum = sum270
                    lst = lst270
                    maps_result = maps270
                    sum_rotate_n = 270    
                    pos = [i,j] 
                else:
                    if (sum_rotate_n==270 and pos[1]>j) or (sum_rotate_n==270 and pos[1]==j and pos[0]>i):
                        first_sum = sum270
                        lst = lst270
                        maps_result = maps270
                        sum_rotate_n = 270    
                        pos = [i,j]               
    #print(pos,sum_rotate_n)
    if first_sum == 0:
        return 0,[],maps
    else:
        return first_sum,lst, maps_result


def rotate90(x,y):
    maps_copy = copy.deepcopy(maps)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue

            if i==x-1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x-1][y] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
    
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate180(x,y):
    maps_copy = copy.deepcopy(maps)

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x+1][y-1] = maps[i][j]
                else:
                    maps_copy[x+1][y] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x][y+1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x+1:
                if j==y-1:
                    maps_copy[x-1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]

    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy

def rotate270(x,y):
    maps_copy = copy.deepcopy(maps)
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            
            if i==x-1:
                if j==y-1:
                    maps_copy[x+1][y-1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y-1] = maps[i][j]
                else:
                    maps_copy[x][y-1] = maps[i][j]
            elif i==x:
                if j==y-1:
                    maps_copy[x+1][y] = maps[i][j]
                else:
                    maps_copy[x-1][y] = maps[i][j]
            elif i==x+1: 
                if j==y-1:
                    maps_copy[x+1][y+1] = maps[i][j]
                elif j==y+1:
                    maps_copy[x-1][y+1] = maps[i][j]
                else:
                    maps_copy[x][y+1] = maps[i][j]
    sum,lst = findFirstVal(maps_copy)

    return sum,lst,maps_copy


def full_lst(lst,maps,full_idx):
    sorted_lst = []
    for k in range(len(lst)):
        for l in range(len(lst[k])):
            sorted_lst.append(lst[k][l])

    sorted_lst.sort(key=lambda x:[x[1],-x[0]])
    
    for m in range(len(sorted_lst)):
        maps[sorted_lst[m][0]][sorted_lst[m][1]] = M_lst[full_idx]
        full_idx += 1

    return maps, full_idx


#main
K, M = map(int,input().split())
maps = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    maps[i] = list(map(int,input().split()))

M_lst = list(map(int,input().split()))

answer_lst = []
full_idx = 0

for k in range(K):
    answer = 0
    #1. 회전
    sum,lst,maps_result = rotate()
    if sum==0:
        break

    maps = maps_result
    #print("maps1",maps)
    #2. 유적 탐사
    while True:
        #유적 카운트
        chain_sum, chain_empty_lst = findFirstVal(maps)
        if chain_sum==0:
            break
        answer += chain_sum
        #유적 채우기
        maps, full_idx = full_lst(chain_empty_lst,maps,full_idx)
        #print("maps2",maps)
    
    #print("ANSWER:",answer)
    if answer != 0:
        answer_lst.append(answer)

print(*answer_lst)