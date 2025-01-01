package BAEKJOON.벽_부수고_이동하기;

import java.io.*;
import java.util.*;

public class Main {
    static class Position{
        int x;
        int y;
        int cnt;
        int d;
        Position(int x, int y, int cnt, int d){
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.d = d;
        }
    }
    static int N, M;
    static int[][] board;
    static boolean[][][] visited;
    static int[][] delta = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    static int bfs(){
        Deque<Position> queue = new ArrayDeque<>();
        queue.add(new Position(0,0, 0, 1));
        visited = new boolean[2][N][M];
        while(!queue.isEmpty()){
            Position pos = queue.pollFirst();
            if(pos.x == N-1 && pos.y == M-1){
                return pos.d;
            }
            for(int[] d : delta){
                int nx = pos.x + d[0];
                int ny = pos.y + d[1];
                if(nx<0 || ny<0 || nx>=N || ny>=M){
                    continue;
                }
                if(board[nx][ny] == 1 && pos.cnt == 0 && visited[1][nx][ny] == false){
                    queue.add(new Position(nx, ny, pos.cnt + 1, pos.d + 1));
                    visited[1][nx][ny] = true;
                }else if(board[nx][ny] == 0){
                    if(pos.cnt == 0 && visited[0][nx][ny] == false){
                        queue.add(new Position(nx, ny, pos.cnt, pos.d + 1));
                        visited[0][nx][ny] = true;
                    }else if(pos.cnt == 1 && visited[1][nx][ny] == false){
                        queue.add(new Position(nx, ny, pos.cnt, pos.d + 1));
                        visited[1][nx][ny] = true;
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        for(int i = 0; i<N; i++){
            String[] str = input.readLine().split("");
            for(int j = 0; j<M; j++){
                board[i][j] = Integer.parseInt(str[j]);
            }
        }
        System.out.println(bfs());
    }
}
