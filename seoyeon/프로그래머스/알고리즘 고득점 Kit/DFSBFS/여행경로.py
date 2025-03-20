#1. 50/100

from collections import defaultdict
def solution(tickets):
    
    answer = []
    tickets.sort()
    visited = [False for _ in range(len(tickets))]
    
    def dfs(start,result,visited):
        if len(result)==len(tickets)+1:
            return result

        for i in range(len(tickets)):
            t = tickets[i]
            if t[0]==start and visited[i]==False:
                tmp = result
                tmp.append(t[1])
                visited[i]=True
                return dfs(t[1],tmp,visited)
                visited[i]=False
    
    answer = dfs("ICN",["ICN"],visited)
    
    return answer

#2. 100/100
from collections import defaultdict
def solution(tickets):
    
    answer = []
    visited = [False for _ in range(len(tickets))]
    
    def dfs(start,result,visited):
        if len(result)==len(tickets)+1:
            answer.append(result)
            return

        for i in range(len(tickets)):
            if tickets[i][0]==start and visited[i]==False:
                visited[i]=True
                dfs(tickets[i][1],result+[tickets[i][1]],visited)
                visited[i]=False
    
    dfs("ICN",["ICN"],visited)
    
    answer.sort()
    
    return answer[0]