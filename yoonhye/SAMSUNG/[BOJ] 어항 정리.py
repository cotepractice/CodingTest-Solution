from collections import deque
import copy
def control(fishes, last) : #어항 배열, 2개이상 쌓여있는 어항 중 가장 마지막 인덱스
    # 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 이 차이를 5로 나눈 몫 = d.
    # if d>0 : 두 어항 중 물고기 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보냄 (이 과정은 모든 인접한 칸에 대해서 동시에 발생)
    move = copy.deepcopy(fishes)
    delta = [(1, 0), (0, 1)]  # 하, 우. 중복을 막기 위해 오른쪽, 아래쪽만 검사
    x_length = len(fishes)

    for x in range(x_length):
        y_length = len(fishes[x])
        for y in range(y_length):
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if ny >= y_length or nx >= x_length or (nx > last and ny >= 1):  # 범위를 벗어난경우
                    continue

                d = abs(fishes[x][y] - fishes[nx][ny]) // 5
                if d > 0:
                    if fishes[x][y] > fishes[nx][ny]:
                        move[x][y] -= d
                        move[nx][ny] += d
                    else:
                        move[x][y] += d
                        move[nx][ny] -= d
    # 이제 다시 어항을 바닥에 일렬로 놓음
    # 가장 왼쪽, 가장 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓는다.
    res = deque([])
    for block in move:
        for fish in block:
            res.append([fish])
    return res

N, K = map(int, input().split())
fishes = deque(list(map(lambda x : [int(x)], input().split())))
sorted_fishes = sorted(fishes)

count = 0
while((sorted_fishes[-1][0] - sorted_fishes[0][0]) > K) :
    count += 1
    smallest = int(1e9)
    plus = []
    for i in range(len(fishes)):
        if fishes[i][0] < smallest:
            plus = [i]
            smallest = fishes[i][0]
        elif fishes[i][0] == smallest:
            plus.append(i)
    for i in plus:  #물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다. 여러개이면 모두 한 마리씩 넣는다.
        fishes[i][0] += 1

    #어항을 쌓는다 =>  가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항 위에 올려놓는다.
    fishes[0] = [fishes[1][0], fishes.popleft()[0]]    #인덱스가 낮을수록 더 아래에 존재.
    last_air = 0
    #2개 이상 쌓여있는 어항을 공중 부양시킨 후, 시계 방향으로 90도 회전시킨 뒤 내려놓는다.
    #공중 부양 시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 놓인 어항이 존재하지 않을 때까지 반복
    while((len(fishes)-last_air-1) >= len(fishes[last_air])):
        length = len(fishes[last_air])
        for i in range(last_air, -1, -1):
            for j in range(0, length):
                fishes[last_air+1+j].append(fishes[i][j])
        for k in range(last_air+1) :
            fishes.popleft()

        last_air = length - 1

    #위에 작업이 모두 끝나면, 어항에 있는 물고기 수 조절 후 바닥에 일렬로 놓음
    fishes = control(fishes, last_air)

    #다시 공중 부양 작업. 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜서 시계 방향으로 180도 회전시킨 다음, 오른쪽 N/2개 위에 놓는다. (2번 반복)
    N = len(fishes)
    j = 0
    for i in range(N-1, (N//2)-1, -1):
        fishes[i].append(fishes[j][0])
        j += 1
    for k in range(N//2):
        fishes.popleft()

    N = N//2
    for j in range(1, -1, -1):
        t = 0
        for i in range((N//2)-1, -1, -1):
            fishes[(N//2)+t].append(fishes[i][j])
            t += 1
    for k in range(N//2):
        fishes.popleft()

    #이 상태에서 다시 위에서 한 물고기 조절 작업 & 일렬로 놓는 작업 수
    fishes = control(fishes, N//2)
    sorted_fishes = sorted(fishes)

print(count)
