#백준 #17144 미세먼지 안녕!
#구현문제
#17:05-
#미해결

r, c, t = map(int, input().split()) #세로 r, 가로 c, t초 지난 후의 결과 도출

origin = [[0 for _ in range(c)] for _ in range(r)]
area = [[0 for _ in range(c)] for _ in range(r)]
circulator = [0, 0]

for i in range(r):
    origin[i] = list(map(int, input().split()))

check = 0
for i in range(r):
    for j in range(c):
        area[i][j] = origin[i][j]
        if (origin[i][j] == -1):
            circulator[check] = [i,j]
            check += 1

#for문
#1. 확산
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(t):
    
    #1. 1초동안 확산
    for i in range(r):
        for j in range(c):
            if (origin[i][j] > 0):
                cnt = 0
                side = 0
                for k in range(4):
                    x = i+dx[k]
                    y = j+dy[k]
                    if (0<=x<r and 0<=y<c):
                        if (origin[x][y] != -1):
                            cnt += 1
                            side = origin[i][j] // 5
                            area[x][y] += side
                area[i][j] -= side*cnt   
    
    #origin과 area 일치
    for i in range(r):
        for j in range(c):
            origin[i][j] = area[i][j]

    #2. 공기 청정기 가동

print(origin)
#2. 공기 청정기 작동
for l in range(2):
    x, y = circulator[l]
    #반시계방향
    if (l == 0):
        area[x][y+1] = 0
        y += 1
        while y<c-1:
            y += 1
            prev = origin[x][y-1]
            area[x][y] = prev
        print(area)
        
        while 0<=x<r:
            x -= 1
            print("x",x,y,origin[x][y])
            prev = origin[x+1][y]
            area[x][y] = prev
        #여기까지 성공. x==0인 경우 이어서 할 것
        
            


print(area)

    #시계방향
    


#출력
# sum = 0
# for i in range(r):
#     for j in range(c):
#         if (origin[i][j] != -1):
#             sum += origin[i][j]
# print(sum)