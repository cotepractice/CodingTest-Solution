#식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값

N = int(input())
foods = list(map(int, input().split()))
dp = [0 for _ in range(len(foods))] #각 원소는 i번째 식량창고까지의 최적의 해. dp[i] = max(foods[i] + dp[i-2], dp[i-1])
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for i in range(2, len(foods)):
    dp[i] = max(foods[i] + dp[i-2], dp[i-1])

print(dp[i])