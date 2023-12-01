# 알고력과 코딩력은 0 이상의 정수
# 알고력/코딩력 1을 높이기 위해서 1의 시간이 필요. 같은 문제를 여러 번 푸는 것이 가능하다.
# 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하여라.
# problems => [필요한 알고력, 필요한 코딩력, 문제를 풀었을 때 증가하는 알고력, 증가하는 코딩력, 문제 푸는데 걸리는 시간]
# 모든 문제를 1번 이상씩 풀 필요는 없다.
def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    queue = []
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(alp_req, max_alp)
        max_cop = max(cop_req, max_cop)

    if max_alp <= alp and max_cop <= cop:
        return 0
    max_alp = max(max_alp, alp)
    max_cop = max(max_cop, cop)
    dp = [[int(1e9) for _ in range(max_cop + 2)] for _ in range(max_alp + 2)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):

            dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue

                dp[min(max_alp, i + alp_rwd)][min(max_cop, j + cop_rwd)] = min(dp[min(max_alp, i + alp_rwd)][min(max_cop, j + cop_rwd)], dp[i][j] + cost)

    return dp[max_alp][max_cop]