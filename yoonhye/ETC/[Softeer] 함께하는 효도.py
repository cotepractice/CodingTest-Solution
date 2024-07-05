import sys

input = sys.stdin.readline


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr, r - 1):
                yield [arr[i]] + next


n, m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

friends = []
for i in range(m):
    x, y = map(int, input().split())
    friends.append((x - 1, y - 1))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

case = combination(d, 3)

first_sum = 0
for x, y in friends:
    first_sum += board[x][y]

total_case = combination(list(case), m)

for c in total_case:
    visited = set(friends)
    status = True
    current_sum = first_sum
    for i in range(m):
        x, y = friends[i]
        for dx, dy in c[i]:
            x, y = x + dx, y + dy
            if x < 0 or y < 0 or x >= n or y >= n:
                status = False
                break
            if (x, y) not in visited:
                current_sum += board[x][y]
                visited.add((x, y))
        if status == False:
            break
    if status == True:
        answer = max(answer, current_sum)

print(answer)