package SWEA.키_순서;

import java.util.*;
import java.io.*;
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static StringTokenizer st;
    static int N, M;
    static Map<Integer, List<Integer>> parent;
    static Map<Integer, List<Integer>> child;
    static int[] check;
    static boolean[] visited;

    static void dfs(int x, Map<Integer, List<Integer>> map){
        for(Integer v : map.get(x)){
            if(visited[v] == false){
                visited[v] = true;
                dfs(v, map);
                check[v]++;
            }
        }
    }
    public static void main(String[] args) throws Exception{
        int T = Integer.parseInt(input.readLine());
        for(int t = 1; t<=T; t++){
            N = Integer.parseInt(input.readLine());
            M = Integer.parseInt(input.readLine());
            check = new int[N+1];
            parent = new HashMap<>();
            child = new HashMap<>();
            for(int i = 1; i<=N; i++){
                parent.put(i, new ArrayList<>());
                child.put(i, new ArrayList<>());
            }
            for(int i = 0; i<M; i++){
                st = new StringTokenizer(input.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                child.get(b).add(a);
                parent.get(a).add(b);
            }

            for(int i = 1; i<=N; i++){
                visited = new boolean[N+1];
                dfs(i, parent);
                visited = new boolean[N+1];
                dfs(i, child);
            }
            int cnt = 0;
            for(int i = 1; i<=N; i++){
                if(check[i] == N-1) cnt++;
            }
            output.append("#").append(t).append(" ").append(cnt).append("\n");
        }
        System.out.println(output.toString());
    }
}
