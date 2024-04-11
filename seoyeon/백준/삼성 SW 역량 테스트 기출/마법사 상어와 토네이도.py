#백준 #20057 마법사 상어와 토네이도
#삼성 SW 역량 테스트 기출

#15:28-

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

print(graph)

tonado_nums = 0 #격자 밖으로 떨어진 모래 양

#2. 이동 위치에 따라 모래 양 변화
def left(graph,start_x,start_y,move_x,move_y,tonado_nums):
    print("left")
    nums = graph[move_x][move_y]

    dx = [-1,1]
    dy = [0,0]

    #1%
    for k in range(2):  #위아래로
        spread_x = start_x + dx[k]
        spread_y = start_y
        #존재한다면 모래양 추가
        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.01)   #해당 위치에 1% 모래 추가
            #graph[spread_y][start_y] += nums*0.01
        #존재하지 않으면 격자 밖으로 떨어진 모래로 간주
        else:
            # print("plus tonado_nums",tonado_nums,nums*0.01)
            tonado_nums += int(nums*0.01)
    #2%
    for k in range(2):
        spread_x = move_x + 2*dx[k]
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.02)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.02)
            tonado_nums += int(nums*0.02)
            

    #7%
    for k in range(2):
        spread_x = move_x + dx[k]
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.07)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.07)
            tonado_nums += int(nums*0.07)

    #10%
    for k in range(2):
        spread_x = move_x + dx[k]
        spread_y = move_y - 1

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.1)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.1)
            tonado_nums += int(nums*0.1)

    #5%
    for k in range(2):
        spread_x = move_x
        spread_y = move_y-2

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.05)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.05)
            tonado_nums += int(nums*0.05)

    return graph, tonado_nums

def right(graph,start_x,start_y,move_x,move_y,tonado_nums):
    print("right")
    nums = graph[move_x][move_y]

    dx = [-1,1]
    dy = [0,0]

    #1%
    for k in range(2):  #위아래로
        spread_x = start_x + dx[k]
        spread_y = start_y
        #존재한다면 모래양 추가
        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.01)   #해당 위치에 1% 모래 추가
            #graph[spread_y][start_y] += nums*0.01
        #존재하지 않으면 격자 밖으로 떨어진 모래로 간주
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.01)
            tonado_nums += int(nums*0.01)


    #2%
    for k in range(2):
        spread_x = move_x + 2*dx[k]
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.02)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.02)
            tonado_nums += int(nums*0.02)
            #print("plus tonado_nums",tonado_nums)

    #7%
    for k in range(2):
        spread_x = move_x + dx[k]
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.07)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.07)
            tonado_nums += int(nums*0.07)
            #print("plus tonado_nums",tonado_nums)
    #10%
    for k in range(2):
        spread_x = move_x + dx[k]
        spread_y = move_y + 1

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.1)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.1)
            tonado_nums += int(nums*0.1)
            #print("plus tonado_nums",tonado_nums)

    #5%
    for k in range(2):
        spread_x = move_x
        spread_y = move_y + 2

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.05)
        else:
            #print("plus tonado_nums",tonado_nums,nums*0.05)
            tonado_nums += int(nums*0.05)
            #print("plus tonado_nums",tonado_nums)

    return graph, tonado_nums

def up(graph,start_x,start_y,move_x,move_y,tonado_nums):
    print("up")
    nums = graph[move_x][move_y]

    dx = [0,0]
    dy = [-1,1]

    #1%
    for k in range(2):  #위아래로
        spread_x = start_x
        spread_y = start_y + dy[k]
        #존재한다면 모래양 추가
        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.01)   #해당 위치에 1% 모래 추가
        #존재하지 않으면 격자 밖으로 떨어진 모래로 간주
        else:
            #print("plus tonado_nums",nums*0.01)
            tonado_nums += int(nums*0.01)

    #2%
    for k in range(2):
        spread_x = move_x
        spread_y = move_y + 2*dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.02)
        else:
            #print("plus tonado_nums",nums*0.02)
            tonado_nums += int(nums*0.02)

    #7%
    for k in range(2):
        spread_x = move_x 
        spread_y = move_y + dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.07)
        else:
            #print("plus tonado_nums",nums*0.07)
            tonado_nums += int(nums*0.07)
    #10%
    for k in range(2):
        spread_x = move_x - 1
        spread_y = move_y + dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.1)
        else:
            #print("plus tonado_nums",nums*0.1)
            tonado_nums += int(nums*0.1)

    #5%
    for k in range(2):
        spread_x = move_x - 2
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.05)
        else:
            #print("plus tonado_nums",nums*0.05)
            tonado_nums += int(nums*0.05)

    return graph, tonado_nums

def down(graph,start_x,start_y,move_x,move_y,tonado_nums):
    print("down")
    nums = graph[move_x][move_y]

    dx = [0,0]
    dy = [-1,1]

    #1%
    for k in range(2):  #위아래로
        spread_x = start_x
        spread_y = start_y + dy[k]
        #존재한다면 모래양 추가
        if 0<=spread_x<N:
            graph[spread_x][spread_y] += int(nums*0.01)   #해당 위치에 1% 모래 추가
        #존재하지 않으면 격자 밖으로 떨어진 모래로 간주
        else:
            #print("plus tonado_nums",nums*0.01)
            tonado_nums += int(nums*0.01)

    #2%
    for k in range(2):
        spread_x = move_x
        spread_y = move_y + 2*dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.02)
        else:
            #print("plus tonado_nums",nums*0.02)
            tonado_nums += int(nums*0.02)

    #7%
    for k in range(2):
        spread_x = move_x 
        spread_y = move_y + dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.07)
        else:
            #print("plus tonado_nums",nums*0.07)
            tonado_nums += int(nums*0.07)
    #10%
    for k in range(2):
        spread_x = move_x + 1
        spread_y = move_y + dy[k]

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.1)
        else:
            #print("plus tonado_nums",nums*0.1)
            tonado_nums += (nums*0.1)

    #5%
    for k in range(2):
        spread_x = move_x + 2
        spread_y = move_y

        if 0<=spread_x<N and 0<=spread_y<N:
            graph[spread_x][spread_y] += int(nums*0.05)
        else:
            #print("plus tonado_nums",nums*0.05)
            tonado_nums += int(nums*0.05)

    return graph, tonado_nums

#def tonado(x,y,nx,ny) => 해당 위치(x,y)에서 이동한 위치(nx,ny)로 이동시의 모래 이동
def tonado(graph,start_x,start_y,move_x,move_y,dx,dy,tonado_nums):
    #print("graph in tonado1",graph)
    #1. 상하좌우 중 어디로 이동하는지 확인
    #좌
    if dx==0 and dy==-1:
        graph, tonado_nums = left(graph,start_x,start_y,move_x,move_y,tonado_nums)
        # print("startx,starty,movex,movey",start_x,start_y,move_x,move_y)
        # print("tonado_nums",tonado_nums)
    #하
    elif dx==1 and dy==0:
        graph, tonado_nums = down(graph,start_x,start_y,move_x,move_y,tonado_nums)
        # print("startx,starty,movex,movey",start_x,start_y,move_x,move_y)
        # print("tonado_nums",tonado_nums)
    #우
    elif dx==0 and dy==1:
        graph, tonado_nums = right(graph,start_x,start_y,move_x,move_y,tonado_nums)
        # print("startx,starty,movex,movey",start_x,start_y,move_x,move_y)
        # print("tonado_nums",tonado_nums)
    #상
    elif dx==-1 and dy==0:
        graph, tonado_nums = up(graph,start_x,start_y,move_x,move_y,tonado_nums)
        # print("startx,starty,movex,movey",start_x,start_y,move_x,move_y)
        # print("tonado_nums",tonado_nums)
    #print("graph in tonado2",graph)
    return graph,tonado_nums

#시작 좌표
start_x = N//2
start_y = N//2

#좌하우상 순서
dx=[0,1,0,-1]
dy=[-1,0,1,0]

#dx,dy는 해당 방향으로 이동. 2번 반복하고 1증가한 횟수만큼 반복을 반복: 1,1,2,2,3,3,4,4,...
k = 0   #dx,dy 인덱스
cnt = 0 #해당 dx,dy 방향으로 "2회 이동"하면 dx,dy 변경
move_n = 1  #cnt를 카운트하기 위해서는 move_cnt가 move_n이 되어야 cnt 1증가
move_cnt = 0    
#한칸씩만 이동한다고 가정 => 추후 해결
while True:
    move_x = start_x + dx[k]
    move_y = start_y + dy[k]
    move_cnt += 1
    # if move_cnt == move_n:
    #     cnt += 1
    #     move_cnt = 0
    #     #방향 변경
    #     k += 1
    #     if k==4:
    #         k = 0
    #print("graph1",graph)
    #모래 이동
    #print("graph1",graph)
    graph,tonado_nums= tonado(graph,start_x,start_y,move_x,move_y,dx[k],dy[k],tonado_nums)
    #print("graph2",graph)

    if move_cnt == move_n:
        cnt += 1
        move_cnt = 0
        #방향 변경
        k += 1
        if k==4:
            k = 0

    #start_x,start_y 변경
    start_x = move_x
    start_y = move_y
    if start_x==0 and start_y==0:
        break
    if cnt == 2:
        move_n += 1
        cnt = 0

#print(tonado_nums)