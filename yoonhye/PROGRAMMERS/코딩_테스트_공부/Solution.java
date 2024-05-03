package PROGRAMMERS.코딩_테스트_공부;

//같은 문제를 여러 번 푸는 것이 가능
//[필요한 알고력, 필요한 코딩력, 증가하는 알고력, 증가하는 코딩력, 시간]
class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;
        int max_alp = 0;
        int max_cop = 0;

        //모든 문제를 푸는데 필요한 알고력, 코딩력 구하기
        for (int i = 0; i < problems.length; i++){
            max_alp = Math.max(max_alp, problems[i][0]);
            max_cop = Math.max(max_cop, problems[i][1]);
        }
        if (max_alp <= alp && max_cop <= cop){
            return 0;
        }

        max_alp = Math.max(alp, max_alp);
        max_cop = Math.max(cop, max_cop);
        int[][] dp = new int[max_alp+2][max_cop+2];
        for (int i = alp; i <= max_alp; i++){
            for (int j = cop; j <= max_cop; j++){
                if (dp[i+1][j] != 0){
                    dp[i+1][j] = Math.min(dp[i+1][j], dp[i][j] + 1);
                } else{
                    dp[i+1][j] = dp[i][j] + 1;
                }
                if (dp[i][j+1] != 0){
                    dp[i][j+1] = Math.min(dp[i][j+1], dp[i][j] + 1);
                } else{
                    dp[i][j+1] = dp[i][j] + 1;
                }
                for (int k = 0; k < problems.length; k++){
                    if (problems[k][0] <= i && problems[k][1] <= j){
                        int a = Math.min(i+problems[k][2], max_alp);
                        int c = Math.min(j+problems[k][3], max_cop);
                        if (dp[a][c] != 0){
                            dp[a][c] = Math.min(dp[a][c], dp[i][j]+problems[k][4]);
                        } else{
                            dp[a][c] = dp[i][j] + problems[k][4];
                        }
                    }
                }
            }
        }

        answer = dp[max_alp][max_cop];

        return answer;
    }
}
