#SWExpertAcademy #1210

# import sys
# sys.stdin = open("input.txt", "r")

#N은 테스트 케이스 N=9를 위한 것
N = 100

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    T = int(input())

    ladders = [[0 for _ in range(N)] for _ in range(N)]
    end = 0 #종료좌표
    
    for i in range(N):
        lst = list(map(int, input().split()))
        ladders[i] = lst
	
    #종료위치 찾기
    for i in range(N):
        if ladders[N-1][i] == 2:
            end = i
    #print("end:",end)

	#종료좌표에서 위로 올라가기
    move = [-1,1] #좌우
    for i in range(N-2,-1,-1):
        #print("i",i)
        check = 0
        for k in range(2):
            if check == 1:
                continue
            move_n = end+move[k]
            #범위 벗어나면 ㅂㅂ
            if move_n<0 or move_n>=N:
                move_n -= move[k]
                continue
            
            while True:
                #사다리가 존재하지 않는 경우 break
                if 0<=move_n<N and ladders[i][move_n] == 0:
                    move_n -= move[k]
                    end = move_n
                    break
                #범위 안에 없는 경우 break
                if move_n<0 or move_n>=N:
                    move_n -= move[k]
                    end = move_n
                    break
                move_n += move[k]
                check = 1
            
    print("#",T," ", end,sep="")