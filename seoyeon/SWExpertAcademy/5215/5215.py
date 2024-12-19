T = int(input())

#제한 칼로리 이하 조합 중 가장 점수가 높은 점수
def cal(idx,flav_n,cal_n):
    global visited, ans
    if cal_n > L:
        return
    ans = max(ans,flav_n)
    
    for i in range(idx+1,N+1):
        if visited[i]==False:
            visited[i] = True
            cal(i,flav_n+flav_cal[i][0], cal_n+flav_cal[i][1])
            visited[i]=False

for t in range(T):
    N, L = map(int, input().split()) #재료개수, 제한 칼로리

    flav_cal = [[0,0] for _ in range(N+1)]

    for i in range(1,N+1):
        TT, KK = map(int, input().split()) #맛, 칼로리
        flav_cal[i] = [TT,KK]
 
    ans = 0
    visited = [False for _ in range(N+1)]
    cal(0, 0, 0)
    print("#",t+1, " ", ans,sep="")