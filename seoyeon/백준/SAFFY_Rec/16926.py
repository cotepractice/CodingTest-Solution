#백준 #16926 배열 돌리기 1

N, M, R = map(int, input().split())

maps = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    lst_i = [0]
    lst = list(map(int,input().split()))
    for k in range(M):
        lst_i.append(lst[k])
    maps[i] = lst_i

def left(x,y):
    return x,y-1

def right(x,y):
    return x,y+1

def up(x,y):
    return x-1,y

def down(x,y):
    return x+1,y

def move(x,y): #depth는 1부터 min(N,M)//2까지 동작, N과 M은 1부터 시작. x와 y는 1부터 시작

        d = min(x,y,N-x+1,M-y+1)

        #up
        if d+1<=x<=N-d+1 and y == M-d+1:
            #print("1",up(x,y))
            return up(x,y)
            
        #down
        if d<=x<=N-d and y == d:
            #print("2",down(x,y))
            return down(x,y)
        #right
        if d<=y<=M-d and x == N-d+1:
            #print("3",right(x,y))
            return right(x,y)

        #left
        if d+1<=y<=M-d+1 and x == d:
            #print("4",left(x,y))
            return left(x,y)



move_maps = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        cur_val = maps[i][j]
        cur_x,cur_y = i,j
        #print("cur",cur_x,cur_y)
        #rotate_N = min(N,M)//2 #문제에 작은게 짝수라고 명시되어 있음
        for r in range(R):
            mv_x, mv_y = move(cur_x,cur_y)
            cur_x,cur_y = mv_x,mv_y
        #print("mv",mv_x,mv_y)
        move_maps[mv_x][mv_y] = cur_val

#print(move_maps)
for i in range(1,N+1):
    for j in range(1,M+1):
        print(move_maps[i][j], end=" ")
    print(end="\n")
