package BAEKJOON.감소하는_수;

import java.util.*;
//10 20 21 30 31 32 40 41 42 50 51 52 53 54 ... 210 310  320 321 3

public class Main {
    public static void main(String[] args) throws Exception{
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        if(N<=10){
            System.out.println(N);
            return;
        }
        List<Long>[] dp = new ArrayList[11];
        for(int i = 0; i<dp.length; i++){
            dp[i] = new ArrayList<>();
        }
        for(long i = 0; i<10; i++){
            dp[1].add(i);
        }
        int k = 1;
        N -= 9;

        while(k<10){
            for(long i = 1; i<10; i++) {
                for (Long num : dp[k]) {
                    if (num / Math.pow(10, k - 1) < i) {
                        dp[k + 1].add(num + i * (long) Math.pow(10, k));
                        N--;
                        if (N == 0) {
                            System.out.println(num + i * (long) Math.pow(10, k));
                            return;
                        }
                    } else {
                        break;
                    }
                }
            }
            k++;
        }
        System.out.println(-1);
    }
}
