package PROGRAMMERS.완주하지_못한_선수;

public class Main {
    public static void main(String[] args){
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};
        Solution solution = new Solution();
        String answer = solution.solution(participant, completion);
        System.out.println(answer);
    }
}
