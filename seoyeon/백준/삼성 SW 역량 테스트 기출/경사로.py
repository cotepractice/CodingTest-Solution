#백준 #14890 경사로 문제
#삼성 SW 역량 테스트 기출
#14:54-15:57
#16:05-16:16


N, L = map(int, input().split())

lst = [[0 for i in range(N)] for i in range(N)]
dp = [[True for i in range(N)] for i in range(N)]

for i in range(N):
    lst[i] = list(map(int, input().split()))

cnt = 0 

#가로 확인
for i in range(N):
    count = 0 #같은 숫자가 반복되는 횟수
    check = True
    idx = -1
    j = 1
    target = lst[i][0]
    while (j<=N-1 and check == True):
        print("target",target,lst[i][j])
        #뒤(현재,j)가 target보다 작은 경우
        if lst[i][j]+1 == target:
            # print("1", check)
            idx = j
            count = 1
            target = lst[i][j]
            print("1", check)
        #뒤(현재,j)가 target보다 큰 경우
        elif lst[i][j]-1 == target:
            # print("2")
            if (count >= L):
                #dp가 False인 경우 체크
                for k in range(L):
                    if (dp[i][j-k-1] == False):
                        check = False
                if (check == True):
                    for k in range(L):
                        dp[i][j-k-1] = False
            else:
                check = False
            print("2", check)

        #앞과 뒤가 같은 경우
        else:
            # print("3")
            count += 1
            # if (idx != -1):
            #     if (count>=L):
            #         for k in range(L):
            #             if (dp[i][idx-k-1] == False):
            #                 check = False
            #                 idx = -1
            #         if (check == True):
            #             for k in range(L):
            #                 dp[i][idx-k-1] = False
            #                 idx = -1
            print("3", check)

        if (j==N-1):
            if (idx != -1):
                if (count>=L):
                    for k in range(L):
                        if (dp[i][idx-k-1] == False):
                            check = False
                            idx = -1
                    if (check == True):
                        for k in range(L):
                            dp[i][idx-k-1] = False
                            idx = -1
                else:
                    check = False

        # print("j",j,check)
        j += 1
    print("check:",check)
    #뒤(현재)가 앞보다 작은 경우, 그 뒤 처리
    if (idx!=-1 and count >= L and check == True):
        for k in range(L):
            if (dp[i][idx-k-1] == False):
                check = False
        if (check == True):
            for k in range(L):
                dp[i][idx-k-1] = False

    if (j == N and check == True):
        cnt += 1

print("cnt:",cnt)
#세로 확인