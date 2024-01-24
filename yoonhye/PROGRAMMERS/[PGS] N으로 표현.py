def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    dp[2] = {N + N, N - N, N // N, N * N, 10 * N + N}

    for i in range(3, 9):  # N의 개수 : 3~8
        n = str(N) * i
        dp[i].add(int(n))
        for j in range(1, i):
            for c in dp[j]:
                for d in dp[i - j]:
                    dp[i].add(c + d)
                    dp[i].add(c - d)
                    dp[i].add(c * d)
                    if d != 0:
                        dp[i].add(c // d)

    for i in range(1, 9):
        for n in dp[i]:
            if number == n:
                return i
    return -1