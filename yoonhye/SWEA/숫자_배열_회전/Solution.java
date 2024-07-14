package SWEA.숫자_배열_회전;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {
    public static int[][] rotate(int[][] arr){
        int N = arr.length;
        int[][] new_arr = new int[N][N];
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                new_arr[j][N-i-1] = arr[i][j];
            }
        }
        return new_arr;
    }
    public static void toString(int[][] arr, String[] answer){
        int N = arr.length;
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                answer[i] += Integer.toString(arr[i][j]);
            }
            answer[i] += " ";
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++){
            int N = Integer.parseInt(br.readLine());
            int[][] board = new int[N][N];
            String[] answer = new String[N];
            for (int i = 0; i<N; i++){
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                answer[i] = "";
            }

            for (int i = 0; i<3; i++){
                board = rotate(board);
                toString(board, answer);
            }

            System.out.printf("#%d\n", test_case);
            for (int i = 0; i<N; i++){
                System.out.println(answer[i]);
            }
        }
    }
}
