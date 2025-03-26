#1. 정확성 76.9 / 100.0 . 테케 3,9,13 실패
from collections import deque

computer_lst=[[]]
visited=[]
N = 0


#x와 y가 연결된 것
def solv(lst):
    global N, computer_lst, visited
    visited = [i for i in range(N)]
    Q=deque()
    for nx,ny in lst:
        Q.append([nx,ny])
    
    while Q:
        i,j = Q.popleft()
        min_val = min(visited[i],visited[j])
        #현재까지 값 업데이트
        for k in range(N):
            if visited[k]==visited[i] or visited[k]==visited[j]:
                visited[k]=min_val
        visited[i],visited[j]=min_val,min_val
        
    
def solution(n, computers):
    answer = 0
    global visited, N, computer_lst
    N = n
    computer_lst=computers
    visited = [False for _ in range(n)]
    
    lst = []
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1 and i<j:
                lst.append([i,j])
    solv(lst)
    solv_dict = dict()
    for i in visited:
        if i not in solv_dict:
            solv_dict[i]=0
            answer += 1
    return answer

#2. 100 => solution의 이중 for문에서 i<j 제거. 단방향 존재 가능

from collections import deque

computer_lst=[[]]
visited=[]
N = 0


#x와 y가 연결된 것
def solv(lst):
    global N, computer_lst, visited
    visited = [i for i in range(N)]
    Q=deque()
    for nx,ny in lst:
        Q.append([nx,ny])
    
    while Q:
        i,j = Q.popleft()
        min_val = min(visited[i],visited[j])
        #현재까지 값 업데이트
        for k in range(N):
            if visited[k]==visited[i] or visited[k]==visited[j]:
                visited[k]=min_val
        visited[i],visited[j]=min_val,min_val
        
    
def solution(n, computers):
    answer = 0
    global visited, N, computer_lst
    N = n
    computer_lst=computers
    visited = [False for _ in range(n)]
    
    lst = []
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1:
                lst.append([i,j])
    solv(lst)
    solv_dict = dict()
    for i in visited:
        if i not in solv_dict:
            solv_dict[i]=0
            answer += 1
    return answer