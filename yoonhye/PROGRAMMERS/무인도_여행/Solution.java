package PROGRAMMERS.무인도_여행;

import java.util.*;

public class Solution {
    static class Node{
        int x;
        int y;
        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    static int[][] delta = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    static int[][] board;
    static int bfs(int x, int y, int R, int C, int[][] visited){
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(x, y));
        int cnt = 0;
        while(!queue.isEmpty()){
            Node node = queue.poll();
            cnt += board[node.x][node.y];
            for(int[] d : delta){
                int nx = node.x + d[0];
                int ny = node.y + d[1];
                if(nx < 0 || nx >= R || ny< 0 || ny >= C){
                    continue;
                }
                if(visited[nx][ny] == 0 && board[nx][ny] >= 0){
                    visited[nx][ny] = 1;
                    queue.add(new Node(nx, ny));
                }
            }
        }
        return cnt;

    }
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        int R = maps.length;
        int C = maps[0].length();
        board = new int[R][C];
        int i = 0, j = 0;
        for(String str : maps){
            String[] arr = str.split("");
            for(String s : arr){
                if(s.equals("X")){
                    board[i][j++] = -1;
                }else{
                    board[i][j++] = Integer.parseInt(s);
                }
            }
            i++;
            j = 0;
        }

        int[][] visited = new int[R][C];
        for(int r = 0; r<R; r++){
            for(int c = 0; c<C; c++){
                if(board[r][c] >= 0 && visited[r][c] == 0){
                    visited[r][c] = 1;
                    answer.add(bfs(r, c, R, C, visited));
                }
            }
        }
        if(answer.size() == 0){
            return new int[]{-1};
        }
        Collections.sort(answer);
        int[] res = new int[answer.size()];
        for(int t = 0; t<answer.size(); t++){
            res[t] = answer.get(t);
        }
        return res;
    }
}
