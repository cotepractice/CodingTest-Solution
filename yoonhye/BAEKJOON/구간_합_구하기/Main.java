package BAEKJOON.구간_합_구하기;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int k = (int) Math.ceil(Math.log(N)/Math.log(2));

        //초기화
        int L = (int) Math.pow(2,(k+1));
        long[] num = new long[L];
        int index = (int) Math.pow(2, k);
        for (int i = 1; i<=N; i++){
            st = new StringTokenizer(br.readLine());
            num[index] = Long.parseLong(st.nextToken());
            index += 1;
        }

        for (int i = L-1; i>0; i--){
            int p = i/2;
            num[p] += num[i];
        }

        for (int i = 1; i<=(M+K); i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            //데이터 업데이트
            if (a==1){
                long c = Long.parseLong(st.nextToken());
                b = (int) Math.pow(2,k) + b - 1;
                long dif = c-num[b];
                num[b] = c;
                b = b/2;
                while(b>0){
                    num[b] += dif;
                    b = b/2;
                }
            }
            //구간합 구하기
            else{
                int c = Integer.parseInt(st.nextToken());
                //위치값 트리구조에 맞게 변경
                b = (int) Math.pow(2,k) + b - 1;
                c = (int) Math.pow(2,k) + c - 1;
                ArrayList<Integer> selected_node = new ArrayList<>();
                while(b<=c){
                    if (b%2 == 1) {
                        selected_node.add(b);
                    }
                    if (c%2 == 0){
                        selected_node.add(c);
                    }
                    b = (b+1)/2;
                    c = (c-1)/2;
                }
                long sum = 0;
                for (Integer n : selected_node){
                    sum += num[n];
                }
                System.out.println(sum);
            }
        }
    }
}
