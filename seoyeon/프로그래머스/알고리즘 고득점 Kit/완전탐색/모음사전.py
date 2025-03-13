#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#모음사전

alpha_words = []
alpha = ["A","E","I","O","U"]

def dfs(depth,word):
    global alpha_words,alpha
    
    alpha_words.append(word)
    
    if len(word)==5:
        return
    
    for al in alpha:
        dfs(depth+1,word+al)

def solution(word):
    answer = 0
    
    for al in alpha:
        dfs(1,al)
    
    answer = alpha_words.index(word)+1
    return answer