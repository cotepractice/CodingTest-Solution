ans = float("inf")

def dfs(cnt,current_word,target,words):
    global ans

    if current_word == target:
        ans = min(ans,cnt)
        return ans
    
    if cnt > len(current_word)+1:
        return
    
    for w in words:
        c = 0
        for i in range(len(w)):
            if current_word[i]!=w[i]:
                c += 1
        if c==1:
            dfs(cnt+1,w,target,words)
    
def solution(begin, target, words):
    global ans
    
    #반환할 수 없는 경우
    if target not in words:
        return 0
    
    dfs(0,begin,target,words)
    
    if ans == float("inf"):
        ans = 0
    
    return ans