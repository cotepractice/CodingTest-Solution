#시계방향으로 회전. i번 칸의 내구도는 Ai.
#1번 칸이 있는 위치: 올리는 위치, N번 칸이 있는 위치 : 내리는 위치
#로봇은 1번 칸에만 올릴 수 있다. 로봇이 N번 위치에 도달하면 그 즉시 내린다.
#로봇은 스스로 이동 가능. 로봇을 1번에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
#로봇들을 건너편으로 옮기는 과정
#1. 벨트가 로봇과 함께 한 칸 회전
#2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동.
#   로봇이 이동하려는 칸에 로봇이 없고, 내구도가 1 이상 남아있어야 해당 칸으로 이동 가능.
#3. 1번 칸의 내구도가 0이 아니면 1번 칸에 로봇을 올림.
#4. 내구도가 0인 칸의 개수가 K개 이상이면 종료. 아니면 반복.
#종료되었을 때 몇 단계가 진행중이었는지 구해보자.
from collections import deque
def rotate():   #벨트가 각 칸 위에 있는 로봇과 함께 회전.
    belt[1].append(belt[0].pop())
    belt[0].appendleft(belt[1].popleft())

    robot.pop()
    robot.appendleft(0)
    robot[-1] = 0   #로봇이 내리는 위치에 도달하면 즉시 내림

def check():
    global N, K
    cnt = 0
    for i in range(2):
        for j in range(N):
            if belt[i][j] == 0:
                cnt += 1
    if cnt >= K:
        return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = [deque(A[:N]), deque(A[:N-1:-1])]
robot = deque([0 for _ in range(N)])
t = 0

while(1):
    t += 1
    #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    rotate()
    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.

    for i in range(N-2, 0, -1):   #1번과정에서 로봇이 이동하기 때문에 로봇이 0번째에는 있을 수 없고, 가장 먼저 벨트에 올라간 로봇은 항상 가장 오른쪽에 존재한다.
        if (robot[i] == 1):   #로봇이 해당 칸에 존재하고,
            if robot[i+1] == 0 and belt[0][i+1] >= 1: #로봇이 이동하려는 칸에 로봇이 없고, 내구도가 1 이상 남아있으면 로봇 이동
                robot[i] = 0
                robot[i+1] = 1
                belt[0][i+1] -= 1

    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0][0] != 0:
        robot[0] = 1
        belt[0][0] -= 1

    #4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if check():
        break

print(t)







