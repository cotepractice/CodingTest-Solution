#1873 상호의 배틀필드

def up():
    current[2]=0
    if 0<=current[0]-1<H and game_maps[current[0]-1][current[1]]==".":
        game_maps[current[0]][current[1]] = "."
        current[0]-=1
    game_maps[current[0]][current[1]] = "^"

def down():
    current[2]=1
    if 0<=current[0]+1<H and game_maps[current[0]+1][current[1]]==".":
        game_maps[current[0]][current[1]] = "."
        current[0]+=1
    game_maps[current[0]][current[1]] = "v"

def left():
    current[2]=2
    if 0<=current[1]-1<W and game_maps[current[0]][current[1]-1]==".":
        game_maps[current[0]][current[1]] = "."
        current[1]-=1
    game_maps[current[0]][current[1]] = "<"

def right():
    current[2]=3
    if 0<=current[1]+1<W and game_maps[current[0]][current[1]+1]==".":
        game_maps[current[0]][current[1]] = "."
        current[1]+=1
    game_maps[current[0]][current[1]] = ">"

def shoot():
    d = current[2]
    cx,cy = current[0],current[1]
    dx,dy = 0,0

    #방향
    if d==0: 
        dx-=1
    elif d==1:
        dx+=1
    elif d==2:
        dy-=1
    elif d==3:
        dy+=1

    while (0<=cx<H and 0<=cy<W):
        
        if game_maps[cx][cy]=="*":
            game_maps[cx][cy]="."
            break
            
        if game_maps[cx][cy]=="#":
            break
        
        cx+=dx
        cy+=dy
    

T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())

    game_maps = ["" for _ in range(H)] #.:평지,*:벽돌벽,#:강철벽,-:물,^,<,>,v:해당 방향을 바라보는 전차

    for h in range(H):
        game_m = list(input())
        game_maps[h] = game_m

    current = [-1,-1,-1] #[x좌표,y좌표,방향]. 방향은 0~3까지 상하좌우
    for i in range(H):
        for j in range(W):
            if game_maps[i][j]=="^":
                current = [i,j,0]
            elif game_maps[i][j]=="v":
                current = [i,j,1]
            elif game_maps[i][j]=="<":
                current = [i,j,2]
            elif game_maps[i][j]==">":
                current = [i,j,3]

    N = int(input())
    actions = input()

    for s in actions:
        if s=="U":
            up()
        elif s=="D":
            down()
        elif s=="L":
            left()
        elif s=="R":
            right()
        elif s=="S":
            shoot()

    print("#",t,sep="",end=" ")
    for h in range(H):
         print(*game_maps[h],sep="")