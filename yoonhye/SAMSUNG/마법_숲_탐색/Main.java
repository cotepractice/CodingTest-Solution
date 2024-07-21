package SAMSUNG.마법_숲_탐색;

import java.util.*;
import java.io.*;

class Position{
    int x;
    int y;
    int d;
    Position(int x, int y, int d){
        this.x = x;
        this.y = y;
        this.d = d;
    }
}
public class Main {
    public static boolean move(int[][] board, int x, int y, int[][] delta){

        int R = board.length;
        int C = board[0].length;
        for (int[] d : delta){
            int nx = x+d[0], ny = y+d[1];
            if (nx<0 || ny<0 || nx>=R || ny>=C || board[nx][ny] > 0){
                return false;
            }
        }
        return true;
    }
    public static int move_g(int[][] board, int n, int K, HashMap<Integer, Position> info){
        int[][] direction = {{-1,0}, {0,1}, {1,0}, {0,-1}};
        int[] visited = new int[K+1];
        int R = board.length;
        int C = board[0].length;

        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(n);

        int max_x = 0;
        while(!queue.isEmpty()){
            int num = queue.poll();
            Position p = info.get(num);
            int x = p.x, y = p.y, d = p.d;
            int ex = direction[d][0] + x, ey = direction[d][1]+ y;

            max_x = Math.max(max_x, x);

            for(int[] dir : direction){
                int nx = dir[0] + ex, ny = dir[1] + ey;
                if (nx < 0 || ny < 0 || nx >= R || ny >= C){
                    continue;
                }
                int new_n = board[nx][ny];
                if (new_n != 0 && visited[new_n] == 0){
                    queue.add(new_n);
                    visited[new_n] = 1;
                }
            }
        }
        return max_x;

    }

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] board = new int[R+3][C];

        int[][] info = new int[K][2];   //info[i][0] : 출발 열, info[i][1] : 출구 방향 정보
        for (int i = 0; i < K; i++){
            st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken())-1;
            info[i][1] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        int[][] delta_down = {{2,0}, {1,1}, {1,-1}};
        int[][] delta_left = {{0,-2}, {-1,-1}, {1,-1}};
        int[][] delta_right = {{0, 2}, {1,1}, {-1,1}};
        int[][] direction = {{-1,0}, {0,1}, {1,0}, {0,-1}};
        HashMap<Integer, Position> g_info = new HashMap<Integer, Position>();

        for(int i = 0; i < K; i++){
            int y = info[i][0];
            int x = 1;
            int d = info[i][1];
            while(true){

                if(move(board, x, y, delta_down)){
                    x++;
                }else{
                    //왼 -> 아래 (출구 반시계방향 이동)
                    if(move(board, x, y, delta_left) && move(board, x, y-1, delta_down)){
                        x++;
                        y--;
                        if (d==0) d = 3;
                        else d--;
                    }else{
                        //오 -> 아래 (출구 시계방향 이동)
                        if(move(board, x, y, delta_right) && move(board, x, y+1, delta_down)){
                            x++;
                            y++;
                            if (d==3) d = 0;
                            else d++;
                        }else{
                            break;
                        }
                    }
                }
            }
            if (x<=3){  //board reset
                board = new int[R+3][C];
                continue;
            }
            //골렘 최종 위치를 board에 남기고 골렘 번호에 따른 출구 정보 저장
            g_info.put(i+1, new Position(x, y, d));

            board[x][y] = i+1;
            for(int[] dir : direction){
                board[x+dir[0]][y+dir[1]] = i+1;
            }

            //정령 이동
            int res = move_g(board, i+1, K, g_info)-1;
            answer += res;

        }
        System.out.println(answer);

    }
}
