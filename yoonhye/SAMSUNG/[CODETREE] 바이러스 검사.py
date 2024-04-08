# 팀장 한 명은 무조건 필요.

n = int(input())  # 식당의 수
customers = list(map(int, input().split()))
check = list(map(int, input().split()))

res = 0
for customer in customers:
    res += 1  # 검사팀장
    rest = customer - check[0]
    if rest <= 0:
        continue

    # 검사팀원
    res += rest // check[1]
    if rest % check[1]:
        res += 1

print(res)