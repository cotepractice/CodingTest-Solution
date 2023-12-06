#상담을 완료하는데 걸리는 시간 = T
#상담시 받을 수 있는 금액 = P
def dfs(i):
    global total, res, board
    total.append(planner[i][1])
    if not board[i]:
        total.pop()
        res.append(sum(total))
        return
    for k in board[i]:
        dfs(k)
    total.pop()

total = []
res = []
N = int(input())
planner = [(0,0)]   #(0,0)은 index 1부터 시작하기 위함
board = [[] for _ in range(N+2)]
for i in range(1,N+1):
    t, p = map(int, input().split())
    planner.append((t, p))
    for j in range(t+i, N+2) :
        board[i].append(j)
planner.append((0,0))

for i in range(1, N+1):
    dfs(i)

print(max(res))
