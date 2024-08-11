package BAEKJOON.미로_탐색;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] maze = new int[N][M];
        for (int i = 0; i < N; i++){
            String[] row = input.readLine().split("");
            for(int j = 0; j < M; j++){
                maze[i][j] = Integer.parseInt(row[j]);
            }
        }

        int[][] arr = new int[N][M];
        boolean[][] visited = new boolean[N][M];
        int[][] delta = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0,0});
        visited[0][0] = true;
        arr[0][0] = 1;
        while(!queue.isEmpty()){
            int[] pos = queue.pop();
            int x = pos[0], y = pos[1];
            for(int[] d : delta){
                int nx = x+d[0];
                int ny = y+d[1];
                if(nx<0 || ny<0 || nx>=N || ny>=M){
                    continue;
                }
                if(visited[nx][ny] == false && maze[nx][ny] == 1){
                    arr[nx][ny] = arr[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        System.out.println(arr[N-1][M-1]);
    }
}
