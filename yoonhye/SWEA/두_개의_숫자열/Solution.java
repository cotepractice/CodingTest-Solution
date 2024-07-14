package SWEA.두_개의_숫자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    public static int solution(int[] short_arr, int[] long_arr){
        int min_length = short_arr.length;
        int max_length = long_arr.length;
        int max_res = 0;
        for (int i=0; i<=max_length-min_length; i++){
            int res = 0;
            int k = 0;
            for (int j=i; j<i+min_length; j++){
                res += short_arr[k++]*long_arr[j];
            }
            max_res = Math.max(res, max_res);
        }
        return max_res;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int test_case=1; test_case<=T; test_case++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] A = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            int[] B = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int answer;
            if (N>=M) {
                answer = solution(B, A);
            } else{
                answer = solution(A, B);
            }
            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}
