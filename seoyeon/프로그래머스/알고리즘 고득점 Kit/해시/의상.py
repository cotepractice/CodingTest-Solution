from collections import defaultdict

def solution(clothes):
    answer = 1
    
    dict = defaultdict(list)
    
    for cloth,type in clothes:
        dict[type].append(cloth)

    n_lst = [] #dict 개수
    for d in dict:
        n_lst.append(len(dict[d]))
        
    #선택하거나 안 하거나
    for i in range(len(n_lst)):
        answer *= (n_lst[i]+1) #가능한 경우의 수(n_lst[i]개) + 아무것도 선택하지 않는 경우 
    
    answer -= 1 #아무것도 선택되지 않는 경우
    
    return answer