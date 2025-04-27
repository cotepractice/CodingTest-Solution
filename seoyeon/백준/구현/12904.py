#백준 #12904 A와B

S = list(input())
T = list(input())

#T->S
answer = 0
def dfs(str):
    global answer
    if len(str)==len(S):
        if str==S:
            answer=1
        return
    if str[-1]=="B":
        dfs(str[:-1][::-1])
    if str[-1]=="A":
        dfs(str[:-1])
    return

dfs(T)
print(answer)