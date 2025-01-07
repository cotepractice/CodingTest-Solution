T = int(input())

def dfs(i,sum):
    global answer, N, B, H_lst
    
    if B <= sum <= answer:
        answer = sum

    if i==N:
        return
    
    for k in range(i,N):
        sum += H_lst[k]
        dfs(k+1,sum)
        sum -= H_lst[k]
    


for t in range(1,T+1):
    N,B = map(int, input().split())
    H_lst = list(map(int, input().split()))

    answer = float("inf")
    dfs(0,0)
    print("#",t , sep ="", end=" ")
    print(answer-B)