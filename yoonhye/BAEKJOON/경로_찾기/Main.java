package BAEKJOON.경로_찾기;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder output = new StringBuilder();

        int N = Integer.parseInt(input.readLine());
        int[][] graph = new int[N][N];
        int[][] res = new int[N][N];
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(input.readLine());
            for(int j = 0; j<N; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
                res[i][j] = graph[i][j];
            }
        }

        for(int k = 0; k<N; k++){
            for(int i = 0; i<N; i++){
                for(int j = 0; j<N; j++){
                    if(res[i][k] + res[k][j] == 2){
                        res[i][j] = 1;
                    }
                }
            }
        }
        for(int i = 0; i<N; i++){
            for(int j = 0; j<N-1; j++){
                output.append(res[i][j]).append(" ");
            }
            output.append(res[i][N-1]);
            if(i != N-1){
                output.append("\n");
            }
        }
        System.out.print(output.toString());
    }
}
