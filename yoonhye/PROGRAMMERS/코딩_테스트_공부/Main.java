package PROGRAMMERS.코딩_테스트_공부;
public class Main {
    public static void main(String[] args){
        Solution solution = new Solution();
        int alp = 10;
        int cop = 10;
        int[][] problems = {{10,15,2,1,2},{20,20,3,3,4}};
        int answer = solution.solution(alp, cop, problems);
        System.out.println(answer);
    }
}
