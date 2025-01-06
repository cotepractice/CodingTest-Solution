T = int(input())

for t in range(1,T+1):

    N = int(input())

    maps = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        maps[n] = list(map(int,input()))
    #print("maps:",maps)

    answer = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if N//2-cnt<=j<=N//2+cnt:
                #print("i,j",i,j)
                answer += maps[i][j]
        if i<N//2:
            cnt += 1
        else:
            cnt -= 1             

    print("#",t,sep="",end=" ")
    print(answer)

