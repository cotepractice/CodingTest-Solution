package BAEKJOON.압축;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        char[] strs = input.readLine().toCharArray();
        Deque<String> queue = new ArrayDeque<>();
        boolean status = false;
        int cnt = 0;
        for(int i = strs.length-1; i>=0; i--){
            if(status){
                queue.addFirst(((strs[i]-'0') * cnt) + "");
                queue.addFirst("+");
                status = false;
            }else{
                if(strs[i]=='('){
                    status = true;
                    cnt = 0;
                    while(!queue.peekFirst().equals(")")){
                        String c = queue.pollFirst();
                        if(c.equals("+")){
                            cnt += Integer.parseInt(queue.pollFirst())-1;
                        }
                        cnt++;
                    }
                    queue.pollFirst();
                }else{
                    queue.addFirst(strs[i]+"");
                }
            }
        }
        int answer = 0;
        while(!queue.isEmpty()){
            String c = queue.pollFirst();
            if(c.equals("+")){
                answer += Integer.parseInt(queue.pollFirst())-1;
            }
            answer++;
        }
        System.out.println(answer);
    }
}
