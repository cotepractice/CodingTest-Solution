package SWEA.파리퇴치3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    public static int spray(int[][] arr, int[][] delta, int M, int x, int y){
        int total = arr[x][y];
        for (int[] d : delta){
            int dx = d[0], dy =d[1];
            for (int i = 1; i<M; i++){
                int nx = x + dx * i;
                int ny = y + dy * i;
                if (nx<0 || ny<0 || nx>=arr.length || ny>=arr.length){
                    continue;
                }
                total += arr[nx][ny];
            }
        }
        return total;
    }
    public static void main(String[] args) throws IOException {
        int[][] delta_plus = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        int[][] delta_x = {{-1,-1}, {-1,1}, {1,1}, {1,-1}};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        System.out.println(T);
        for (int t = 1; t<=T; t++){

            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] board = new int[N][N];
            for (int i=0; i<N; i++){
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }

            int answer = 0;
            for (int i = 0; i<N; i++){
                for (int j = 0; j<N; j++){
                    answer = Math.max(answer, spray(board, delta_plus, M, i, j));
                    answer = Math.max(answer, spray(board, delta_x, M, i, j));
                }
            }
            System.out.printf("#%d %d\n", t, answer);
        }

    }
}
