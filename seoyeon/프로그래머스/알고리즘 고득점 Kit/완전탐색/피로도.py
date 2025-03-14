#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#피로도

from itertools import permutations

K = -1
ans = 0

#cnt는 
def dfs(current_power,cnt,idx,visited,dungeons):
    global ans

    ans = max(ans,cnt)
    
    for i in range(idx+1,len(dungeons)):
        if visited[i] == False:
            if current_power>=dungeons[i][0]:
                visited[i]=True
                dfs(current_power-dungeons[i][1], cnt+1,i,visited,dungeons)
                visited[i]=False

def solution(k, dungeons):
    global K, ans
    visited = [False for _ in range(k+1)]
    
    K = k
    lst = permutations(dungeons,len(dungeons))
    for l in lst:
        dfs(k,0,-1,visited,l)
    
    return ans