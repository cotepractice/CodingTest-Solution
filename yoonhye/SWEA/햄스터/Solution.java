package SWEA.햄스터;

import java.util.*;
import java.io.*;

//가능한 경우 중 햄스터 수가 가장 많은 것을 출력. & 사전순으로 더 앞선 순서.

class Solution{
    public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static StringBuilder output = new StringBuilder();
    public static StringTokenizer st;
    public static List<Integer> res;
    public static int maxSum;
    public static int[][] memo;
    public static void combination(int X, int r, List<Integer> temp) {
        if(r == 0) {
            if(check(temp)) {
                compare(temp);
            }
            return;
        }
        for(int i = 0; i<= X; i++) {
            temp.add(i);
            combination(X, r-1, temp);
            temp.remove(temp.size()-1);
        }
    }
    public static boolean check(List<Integer> lst) {
        boolean success = true;
        for(int[] message : memo) {
            int cnt = 0;
            for(int i = message[0]-1; i < message[1]; i++) {
                cnt += lst.get(i);
            }
            if(cnt != message[2]) { //햄스터 수가 일치하지 않으면
                success = false;
                break;
            }
        }
        return success;
    }
    public static void compare(List<Integer> lst) {
        int sum = 0;
        for(Integer value : lst) {
            sum += value;
        }
        if(maxSum < sum) {
            res = new ArrayList<>(lst);
            maxSum = sum;
        }else if(sum == 0) {
            res = new ArrayList<>(lst);
        }
    }
    public static void main(String args[]) throws Exception{

        int T = Integer.parseInt(input.readLine());

        for(int test_case = 1; test_case <= T; test_case++)
        {
            st = new StringTokenizer(input.readLine());
            int N = Integer.parseInt(st.nextToken());
            int X = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            res = new ArrayList<>();
            memo = new int[M][3];
            maxSum = 0;
            for(int i = 0; i<M; i++) {
                st = new StringTokenizer(input.readLine());
                for(int j = 0; j<3; j++) {
                    memo[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            combination(X, N, new ArrayList<Integer>());

            output.append("#").append(test_case).append(" ");
            if(res.size() != 0) {
                for(Integer value : res) {
                    output.append(value).append(" ");
                }
            }else {
                output.append(-1);
            }
            output.append("\n");
        }
        System.out.println(output.toString());
    }
}