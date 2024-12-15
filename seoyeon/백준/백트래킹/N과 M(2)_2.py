#백준 #15650 N과 M(2)

N, M = map(int, input().split())

def backtracking(n, ans):

    if len(ans)== M:
        print(*ans)
        return
    
    for i in range(n,N+1):
        ans.append(i)
        #print("1",ans)
        backtracking(i+1,ans)
        ans.pop()
        #print("2",ans)


ans = []
backtracking(1, ans)