#프로그래머스

#1. 알고리즘 DFS 완전 탐색 => 정확도 4.5
def graph(start,end,visited,edges,check):
    global final_n
    
    if start>final_n:
        final_n = start
    elif end>final_n:
        final_n = end
        
    #print("s",start,visited[start],"e",end,visited[end],check)
    lst1 = []
    lst2 = []
    visited[start] += 1
    
    #도넛 그래프 종결 (N=1)
    if start == end:
        return 1
    
    #반복
    if visited[end]==1:
        if check==0:
            return 1
        else:
            return 3
    
    #현재 end에서 이동할 정점 찾기. 다음 graph()

    for i in range(len(edges)):
        if edges[i][0]==end:
            if visited[edges[i][1]] == 0:
                lst1.append([edges[i][0], edges[i][1]])
            else:
                lst2.append([edges[i][0], edges[i][1]])
    
    if len(lst1)+len(lst2)==0:
        visited[end] += 1
        return 2
    elif len(lst1)+len(lst2)==1:
        if len(lst1)==1:
            return graph(lst1[0][0], lst1[0][1], visited, edges, check)
        else:
            return graph(lst2[0][0], lst2[0][1], visited, edges, check)
    else:
        check = 1
        if len(lst1)>=1:
            return graph(lst1[0][0], lst1[0][1], visited, edges, check)
        else:
            return graph(lst2[0][0], lst2[0][1], visited, edges, check)

def solution(edges):
    visited = [0 for _ in range(len(edges)+1)]
    global final_n 
    max_n = 0
    n_lst = [0 for _ in range(len(edges)+1)]
    for i in range(len(edges)):
        n_lst[edges[i][0]] += 1
        if (n_lst[max_n] < n_lst[edges[i][0]]):
            max_n = edges[i][0]
    result_lst = [max_n,0,0,0]
    
    for k in range(len(edges)):
        
        if edges[k][0] == max_n:
            continue
        
        if visited[edges[k][0]] == False:

            result = graph(edges[k][0],edges[k][1],visited,edges,0)
            #print("r",result)
            if result==-1 or result == None:
                return -1
            result_lst[result] += 1
            
    for k in range(1, final_n+1):
        if k!=max_n and visited[k] == 0:
            print("k",k)
            result_lst[2] += 1
    
    return result_lst

final_n = 0

#2. dictionary 사용 => 정확도 100\\\\\\\\\\\\\\\\\-

def solution(edges):

    dict = {}   #dict는 {a: [n,m]}으로 n은 나가는 간선 수, m은 들어가는 간선 수
    
    #들어오고 나가는 간선 수
    for a,b in edges:
        if not dict.get(a):
            dict[a] = [0,0]
        if not dict.get(b):
            dict[b] = [0,0]
        
        dict[a][0] += 1
        dict[b][1] += 1
    
    #간선 수에 따라 정점 선택 
    answer = [0,0,0,0]
    for key,cnt in dict.items():
        if cnt[0]>=2 and cnt[1]==0:
            answer[0] = key
        elif cnt[0]==0 and cnt[1]>0:
            answer[2] += 1
        elif cnt[0]>=2 and cnt[1]>=2:
            answer[3] += 1
    
    #도넛 모양 그래프는 전체 개수(생성된 정점은 모든 그래프의 개수만큼 나가는 간선 존재)에서 막대 모양과 8자 모양 그래프를 뺀 값
    answer[1] = dict[answer[0]][0] - answer[2] - answer[3]
    
    return answer