MOD = 100000007

# 테이블 줄 수 N과 열 수 M을 입력받음
N = int(input())
M = 3  # 열의 개수 (여기서는 3열 격자로 설정)

# 가능한 상태 수
max_state = 1 << M

# dp 배열 설정
dp = [[0] * max_state for _ in range(N + 1)]

# 첫 줄 초기화
dp[0][0] = 1

# 비트마스크를 통해 연속된 자리 확인
def is_valid(state, M):
    # 두 연속된 1이 있는 경우 False
    return not any(((state >> i) & 3) == 3 for i in range(M - 1))

# 가능한 앉음의 상태 전이
for i in range(1, N + 1):
    for j in range(max_state):  # 현재 줄의 상태
        if not is_valid(j, M):  # 인접한 자리 규칙에 맞지 않는 경우
            continue

        for k in range(max_state):  # 이전 줄의 상태
            if not is_valid(k, M):  # 인접한 자리 규칙에 맞지 않는 경우
                continue

            # 현재 상태와 이전 상태가 겹치지 않는지 확인
            if (j & k) == 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

# 최종 경우의 수 계산
result = sum(dp[N]) % MOD
print(result)