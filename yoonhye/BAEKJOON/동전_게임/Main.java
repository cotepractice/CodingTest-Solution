package BAEKJOON.동전_게임;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] board;
    static int minCnt;
    static boolean check(){
        boolean status = board[0][0];
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                if(board[i][j] != status){
                    return false;
                }
            }
        }
        return true;
    }
    static void reverse(int type, int n){
        switch(type){
            case 1:
                for(int i = 0; i<3; i++){
                    board[n][i] = !board[n][i];
                }
                return;
            case 2:
                for(int i = 0; i<3; i++){
                    board[i][n] = !board[i][n];
                }
                return;
            case 3:
                for(int i = 0; i<3; i++){
                    board[i][i] = !board[i][i];
                }
                return;
            case 4:
                for(int i = 0; i<3; i++){
                    board[i][2-i] = !board[i][2-i];
                }
                return;
        }
    }
    static void dfs(int type, int n, int cnt){
        if(cnt > 8 || cnt>=minCnt){
            return;
        }
        if(check()){
            minCnt = Math.min(minCnt, cnt);
            return;
        }

        for(int i = 1; i<=2; i++){
            for(int j = 0; j<3; j++){
                if(type == i && n == j){
                    continue;
                }
                reverse(i, j);
                dfs(i, j, cnt+1);
                reverse(i, j);
            }
        }
        if(type!= 3){
            reverse(3, 0);
            dfs(3, 0, cnt+1);
            reverse(3, 0);
        }
        if(type != 4){
            reverse(4, 0);
            dfs(4, 0, cnt+1);
            reverse(4, 0);
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(input.readLine());
        for(int t = 0; t<T; t++){
            board = new boolean[3][3];
            minCnt = 10000;
            for(int i = 0; i<3; i++){
                st = new StringTokenizer(input.readLine());
                for(int j = 0; j<3; j++){
                    String s = st.nextToken();
                    if(s.equals("T")){
                        board[i][j] = true;
                    }else{
                        board[i][j] = false;
                    }
                }
            }
            dfs(0, 0, 0);
            if(minCnt == 10000){
                output.append(-1).append("\n");
            }else{
                output.append(minCnt).append("\n");
            }
        }
        System.out.println(output.toString());
    }
}
