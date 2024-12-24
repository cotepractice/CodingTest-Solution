package SWEA.암호생성기;

import java.util.*;
import java.io.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static StringTokenizer st;
    static int minCnt;
    static Deque<Integer> queue;

    public static void main(String[] args) throws Exception{
        for(int t = 1; t<=10; t++) {
            int T = Integer.parseInt(input.readLine());
            minCnt = Integer.MAX_VALUE;
            queue = new ArrayDeque<>();
            st = new StringTokenizer(input.readLine());
            for(int i = 0; i<8; i++){
                int value = Integer.parseInt(st.nextToken());
                int cnt = value / 15;
                minCnt = Math.min(minCnt, cnt);
                queue.add(value);
            }

            for(int i = 0; i<queue.size(); i++) {
                int value = queue.pop();
                value -= (minCnt-1) * 15;
                queue.add(value);
            }

            boolean status = true;
            while(status){
                for(int i = 1; i<=5; i++){
                    int value = (queue.pop() - i);
                    if(value<=0){
                        status = false;
                        queue.add(0);
                        break;
                    }
                    queue.add(value);
                }
            }
            output.append("#").append(T).append(" ");
            while(!queue.isEmpty()){
                output.append(queue.pop()).append(" ");
            }
            output.append("\n");
        }
        System.out.println(output.toString());
    }
}

