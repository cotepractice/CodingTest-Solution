package BAEKJOON.탈출;

//고슴도치 : S, 비버의 굴 : D, 물 : *, 돌 : X
//물과 고슴도치는 돌을 통과할 수 없다.
//고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
//고슴도치가 비버의 굴로 이동하기 위해 필요한 최소 시간.
//고슴도치는 다음 시간에 물이 찰 예정인 칸으로 이동할 수 없음.

import java.util.*;
import java.io.*;

public class Main {
    static class Position{
        int x;
        int y;
        int t;
        Position(int x, int y){
            this.x = x;
            this.y = y;
        }
        Position(int x, int y, int t){
            this.x = x;
            this.y = y;
            this.t = t;
        }
    }
    static int R, C;
    static char[][] map;
    static int dx, dy, sx, sy;
    static Deque<Position> waters;
    static int[][] delta = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    static void waterMove(){
        int len = waters.size();
        for(int i = 0; i<len; i++){
            Position pos = waters.pollFirst();
            for(int[] d : delta){
                int nx = pos.x + d[0];
                int ny = pos.y + d[1];
                if(nx<0 || ny<0 || nx>=R || ny>=C || map[nx][ny] == 'X' || map[nx][ny] == 'D' || map[nx][ny] == '*'){
                    continue;
                }
                map[nx][ny] = '*';
                waters.add(new Position(nx, ny));
            }
        }
    }
    static int move(){
        Deque<Position> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[R][C];
        visited[sx][sy] = true;
        queue.add(new Position(sx, sy, 0));
        int t = -1;
        while(!queue.isEmpty()){
            Position pos = queue.pollFirst();
            if (t != pos.t){
                t = pos.t;
                waterMove();
            }
            for(int[] d : delta){
                int nx = pos.x + d[0];
                int ny = pos.y + d[1];
                if(nx == dx && ny == dy){
                    return pos.t+1;
                }
                if(nx<0 || ny<0 || nx>=R || ny>=C || map[nx][ny] == '*' || map[nx][ny] == 'X' || visited[nx][ny]){
                    continue;
                }
                queue.add(new Position(nx, ny, pos.t+1));
                visited[nx][ny] = true;
            }
        }
        return -1;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        waters = new ArrayDeque<>();
        for(int i = 0; i<R; i++){
            String str = input.readLine();
            map[i] = str.toCharArray();
            for(int j = 0; j<C; j++){
                if(map[i][j] == '*'){
                    waters.add(new Position(i, j));
                }else if(map[i][j] == 'S'){
                    sx = i;
                    sy = j;
                }else if(map[i][j] == 'D'){
                    dx = i;
                    dy = j;
                }
            }
        }
        int res = move();
        if(res == -1){
            System.out.println("KAKTUS");
        }else{
            System.out.println(res);
        }
    }
}
