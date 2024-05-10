def get_dp(arr1, arr2, number):
    s = set()
    for i in arr1:
        for j in arr2:
            s.add(i + j)
            s.add(abs(i - j))
            if j != 0:
                s.add(i // j)
            if i != 0:
                s.add(j // i)
            s.add(i * j)
    return s


def solution(N, number):
    answer = 0
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    dp[1] = set({N})
    for i in range(2, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            s = get_dp(dp[j], dp[i - j], number)
            dp[i] = dp[i].union(s)
        if number in dp[i]:
            return i

    return -1