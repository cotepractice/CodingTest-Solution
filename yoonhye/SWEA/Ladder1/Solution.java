package SWEA.Ladder1;
import java.util.*;
import java.io.*;

class Solution{
    public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static StringBuilder output = new StringBuilder();
    public static StringTokenizer st;
    public static final int N = 100;
    public static int[][] board = new int[N][N];
    public static boolean[][] visited;
    public static int[][] delta = {{0,1}, {0,-1}, {-1,0}};

    public static int dfs(int end) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {N-1, end});
        while(!queue.isEmpty()) {
            int[] pos = queue.pollLast();
            int x = pos[0], y = pos[1];
            visited[x][y] = true;
            if(x == 0) {
                return y;
            }
            for(int[] d: delta){
                int nx = x + d[0], ny = y + d[1];
                if(nx<0 || ny<0 || nx>=N || ny>=N){
                    continue;
                }
                if(!visited[nx][ny] && board[nx][ny] == 1){
                    queue.add(new int[] {nx, ny});
                    break;
                }
            }
        }
        return -1;

    }
    public static void main(String args[]) throws Exception {

        for(int test_case = 1; test_case <= 10; test_case++){
            int T = Integer.parseInt(input.readLine());
            visited = new boolean[N][N];
            int end = 0;
            for(int i = 0; i<N; i++) {
                st = new StringTokenizer(input.readLine());
                for (int j = 0; j<N; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                    if(board[i][j] == 2) {
                        end = j;
                    }
                }
            }
            output.append("#").append(T).append(" ");
            int res = dfs(end);
            output.append(res).append("\n");
        }
        System.out.println(output.toString());
    }
}