package BAEKJOON.포스택;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        StringTokenizer st = new StringTokenizer(input.readLine());

        Deque<Integer>[] stacks = new ArrayDeque[4];
        for(int i = 0; i<4; i++){
            stacks[i] = new ArrayDeque<>();
        }
        for(int i = 0; i<N; i++){
            boolean status = false;
            int n = Integer.parseInt(st.nextToken());
            for(int j = 0; j<4; j++){
                if(stacks[j].isEmpty()){
                    stacks[j].add(n);
                    status = true;
                    break;
                }else{
                    if(stacks[j].peekLast() < n){
                        stacks[j].add(n);
                        status = true;
                        break;
                    }
                }
            }
            if(!status){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
