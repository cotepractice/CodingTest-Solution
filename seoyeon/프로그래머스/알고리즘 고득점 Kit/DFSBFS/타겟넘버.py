

target_n = 0
ans = 0
numbers_lst = []

def dfs(idx,current):
    global ans
        
    if idx==len(numbers_lst):
        if current == target_n:
            ans+=1
            return
        else:
            return
    dfs(idx+1,current+numbers_lst[idx])
    dfs(idx+1,current-numbers_lst[idx])

def solution(numbers, target):
    global target_n, ans, numbers_lst
    
    target_n = target
    numbers_lst = numbers
    
    dfs(0,0)
    
    return ans