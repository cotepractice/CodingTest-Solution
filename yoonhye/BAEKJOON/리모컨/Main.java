package BAEKJOON.리모컨;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static Set<Integer> numSet = new HashSet<>();
    static int[] numArr;
    static int minValue;
    static Map<Integer, Integer> map = new HashMap<>(){{
        put(100, 0);
        put(101, 1);
        put(102, 2);
        put(103, 3);
        put(99, 1);
        put(98, 2);
    }};
    static void combination(int len, int r, List<Integer> lst){
        if(r == 0){
            int num = 0;
            for(int i = 0; i<lst.size(); i++){
                num += lst.get(i) * Math.pow(10, i);
            }
            minValue = Math.min(minValue, Math.abs(N-num) + len);
            return;
        }

        for(int i = 0; i<numArr.length; i++){
            lst.add(numArr[i]);
            combination(len, r-1, lst);
            lst.remove(lst.size()-1);
        }

    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String strN = input.readLine();
        N = Integer.parseInt(strN);
        int M = Integer.parseInt(input.readLine());

        for(int i = 0; i<10; i++){
            numSet.add(i);
        }
        if(M>0){
            StringTokenizer st = new StringTokenizer(input.readLine());

            for(int i = 0; i<M; i++){
                numSet.remove(Integer.parseInt(st.nextToken()));
            }
        }
        if(map.containsKey(N)){
            System.out.println(map.get(N));
            return;
        }

        if(numSet.size() == 1 && numSet.contains(0)){
            System.out.println(Math.min(Math.abs(N-100), Math.abs(0-N) + 1));
            return;
        }else if(numSet.size() == 0){
            System.out.println(Math.abs(N-100));
            return;
        }

        numArr = new int[numSet.size()];
        int index = 0;
        for(int n : numSet){
            numArr[index++] = n;
        }
        boolean status = true;
        int len = strN.length();
        char[] arrN = strN.toCharArray();
        for(int i = 0; i<len; i++){
            int n = arrN[i]-'0';
            if(!numSet.contains(n)){
                status = false;
                break;
            }
        }
        if(status){
            System.out.println(strN.length());
        }else{
            minValue = Math.abs(N-100);

            if(len > 1){
                combination(len-1, len-1, new ArrayList<>());
            }
            combination(len, len, new ArrayList<>());
            combination(len+1, len+1, new ArrayList<>());
            System.out.println(minValue);
        }
    }
}

