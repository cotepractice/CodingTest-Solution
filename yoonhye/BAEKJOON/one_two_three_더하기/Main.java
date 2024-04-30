package BAEKJOON.one_two_three_더하기;

import java.util.*;

//dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
public class Main {
    public static void main(String[] args){
        int[] dp = new int[11];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i<=10; i++){
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
        }
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i<T; i++){
            int n = sc.nextInt();
            System.out.println(dp[n]);
        }
    }
}
