package BAEKJOON.탑;

import java.util.*;
import java.io.*;

public class Main {
    static class Tower{
        int height;
        int index;
        Tower(int height, int index){
            this.height = height;
            this.index = index;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();
        int N = Integer.parseInt(input.readLine());
        Tower[] towers = new Tower[N+1];
        StringTokenizer st = new StringTokenizer(input.readLine());
        for(int i = 1; i<=N; i++){
            towers[i] = new Tower(Integer.parseInt(st.nextToken()), i);
        }

        Deque<Tower> queue = new ArrayDeque<>();
        int[] answer = new int[N+1];
        queue.add(towers[N]);
        for(int i = N-1; i>0; i--){
            Tower t = towers[i];
            while(!queue.isEmpty() && queue.peekFirst().height <= t.height){
                answer[queue.pollFirst().index] = t.index;
            }
            queue.addFirst(t);
        }

        for(int i = 1; i<=N; i++){
            output.append(answer[i]).append(" ");
        }
        System.out.println(output.toString());
    }
}
