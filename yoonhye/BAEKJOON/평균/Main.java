package BAEKJOON.평균;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        double sum = 0;
        double M = 0;
        for (int i=0; i<N; i++){
            double num = Double.parseDouble(st.nextToken());
            sum += num;
            M = Math.max(num, M);
        }
        double avg = sum/N;
        double new_avg = (avg/M)*100;

        System.out.println(new_avg);
    }
}
