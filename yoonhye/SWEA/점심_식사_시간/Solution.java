package SWEA.점심_식사_시간;

import java.util.*;
import java.io.*;

public class Solution {
    static class Person{
        int x;
        int y;
        int t;
        Person(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    static class Stair{
        int x;
        int y;
        int d;
        List<Person> down;
        List<Person> waiting;
        Stair(int x, int y, int d){
            this.x = x;
            this.y = y;
            this.d = d;
        }

    }
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static StringTokenizer st;
    static int N;
    static int[][] board;
    static List<Person> people;
    static Stair[] stairs;
    static int time;
    static boolean[] check;

    static int getDistance(int x1, int y1, int x2, int y2){
        return Math.abs(x1-x2) + Math.abs(y1-y2);
    }
    static void combi(int cnt){
        if(cnt == people.size()){
            for(Stair s : stairs){
                s.down = new ArrayList<>();
                s.waiting = new ArrayList<>();
            }
            for(int i = 0; i<people.size(); i++){
                Person p = people.get(i);
                if(check[i]){
                    p.t = getDistance(p.x, p.y, stairs[0].x, stairs[0].y);
                    stairs[0].waiting.add(people.get(i));
                }else{
                    p.t = getDistance(p.x, p.y, stairs[1].x, stairs[1].y);
                    stairs[1].waiting.add(people.get(i));
                }
            }
            int t = Math.max(move(stairs[0]), move(stairs[1]));
            time = Math.min(time, t);
            return;
        }

        combi(cnt+1);
        check[cnt] = true;
        combi(cnt+1);
        check[cnt] = false;
    }

    static int move(Stair s){
        int t = 0;
        while(!s.waiting.isEmpty() || !s.down.isEmpty()){
            t++;
            for(int i = 0; i<Math.min(3, s.down.size()); i++){
                Person p = s.down.get(i);
                p.t--;
                if(p.t == 0){
                    s.down.remove(i--);
                }
            }
            for(int i = 0; i<s.waiting.size(); i++) {
                Person p = s.waiting.get(i);
                p.t--;
                if (p.t == 0) {
                    p.t = s.d + 1;
                    s.down.add(p);
                    s.waiting.remove(i--);
                }
            }
        }
        return t;
    }

    public static void main(String[] args) throws Exception {
        int T = Integer.parseInt(input.readLine());
        for(int t = 1; t<=T; t++){
            N = Integer.parseInt(input.readLine());
            board = new int[N][N];
            people = new ArrayList<>();
            stairs = new Stair[2];
            int n = 0;
            for(int i = 0; i<N; i++){
                st = new StringTokenizer(input.readLine());
                for(int j = 0; j<N; j++){
                    board[i][j] = Integer.parseInt(st.nextToken());
                    if(board[i][j] == 1){
                        people.add(new Person(i, j));
                    }else if (board[i][j] > 1){
                        stairs[n++] = new Stair(i, j, board[i][j]);
                    }
                }
            }
            time = Integer.MAX_VALUE;
            check = new boolean[people.size()];
            combi(0);
            output.append("#").append(t).append(" ").append(time).append("\n");
        }
        System.out.println(output.toString());
    }
}
