package SAMSUNG.코드트리_투어;

import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder output = new StringBuilder();
    static int[][] graph;
    static HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
    static int[] info;
    static PriorityQueue<Product> products;
    static HashSet<Integer> productsId = new HashSet<>();
    static int MAX_VALUE = 1_000_001;


    static class Product {
        private int id;
        private int revenue;
        private int dest;
        private int cost;

        Product(int id, int revenue, int dest, int cost){
            this.id = id;
            this.revenue = revenue;
            this.dest = dest;
            this.cost = cost;
        }

    }

    static class Node{
        private int number;
        private int cost;

        Node(int number, int cost){
            this.number = number;
            this.cost = cost;
        }
    }

    //200 id revenue dest
    //여행 상품을 추가로 만들고 이를 관리 목록에 추가
    public static void make(int id, int revenue, int dest) {
        Product product = new Product(id, revenue, dest, info[dest]);
        productsId.add(id);
        products.add(product);
    }
    //300 id
    //id에 해당하는 여행 상품이 존재하는 경우 해당 id의 여행 상품을 관리 목록에서 삭제
    public static void cancel(int id) {
        productsId.remove(id);
    }
    //400
    //최적의 여행 상품 id 출력 후 관리 목록에서 제거. 조건을 만족하는 상품이 없다면 -1 출력.
    //관리 목록에서 조건에 맞는 최적의 여행 상품을 선택하여 판매.
    //선택 조건 = [revenue - cost]가 최대인 상품을 우선적으로 고려.
    //같은 값을 가지는 상품이 여러 개 있을 경우 id가 가장 작은 상품 선택
    //cost = 출발지로부터 도착지까지 도달하기 위한 최단거리.
    //만약 출발지에서 dest로 도달할 수 없거나, cost가 revenue보다 더 큰 경우 판매 불가 상품이 됨.
    public static int sell() {
        while(!products.isEmpty()){
            Product product = products.peek();
            if(!productsId.contains(product.id)){
                products.poll();
                continue;
            }
            if(product.cost == MAX_VALUE || product.revenue < product.cost){
                return -1;
            }else{
                products.poll();
                return product.id;
            }
        }
        return -1;
    }
    //500 s
    //여행 상품의 출발지는 전부 s로 변경. 출발지가 변경됨에 따라 각 상품의 cost가 변경될 수 있음
    public static void change(int s, int n) {
        getShortestDistance(s, n);
        PriorityQueue<Product> newProducts = new PriorityQueue<>(new Comparator<Product>(){
            @Override
            public int compare(Product p1, Product p2){
                int b1 = p1.revenue - p1.cost;
                int b2 = p2.revenue - p2.cost;
                if(b1 == b2){
                    return Integer.compare(p1.id, p2.id);
                }else{
                    return Integer.compare(b2, b1);
                }
            }
        });
        for(Product p : products){
            p.cost = info[p.dest];
            newProducts.add(p);
        }
        products = newProducts;

    }

    public static void getShortestDistance(int start, int n) {
        //info 초기화
        for(int i = 0; i<n; i++){
            info[i] = MAX_VALUE;
        }
        info[start] = 0;

        int[] visited = new int[n];
        PriorityQueue<Node> queue = new PriorityQueue<>(new Comparator<Node>(){
            @Override
            public int compare(Node n1, Node n2){
                return Integer.compare(n1.cost, n2.cost);
            }
        });
        queue.add(new Node(start, 0));
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int num = node.number;
            int cost = node.cost;
            if(cost > info[num]){
                continue;
            }
            for(Integer adj : map.get(num)) {
                if(info[adj] > cost + graph[num][adj]) {
                    info[adj] = cost + graph[num][adj];
                    queue.add(new Node(adj, info[adj]));
                }

            }
        }
    }

    public static void main(String[] agrs) throws Exception{
        int Q = Integer.parseInt(input.readLine());
        st = new StringTokenizer(input.readLine());
        int req = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        info = new int[n];

        //graph, map 초기화
        for(int i = 0; i<n; i++) {
            map.put(i, new ArrayList<Integer>());
            for(int j = 0; j<n; j++){
                if(i == j) {
                    graph[i][j] = 0;
                }else{
                    graph[i][j] = MAX_VALUE;
                }
            }
        }
        for(int i = 0; i<m; i++) {
            int v = Integer.parseInt(st.nextToken());
            int u = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[v][u] = Math.min(graph[v][u], w);
            graph[u][v] = Math.min(graph[u][v], w);
            map.get(v).add(u);
            map.get(u).add(v);
        }

        int start = 0;
        getShortestDistance(start, n);


        products = new PriorityQueue<>(new Comparator<Product>(){
            @Override
            public int compare(Product p1, Product p2){
                int b1 = p1.revenue - p1.cost;
                int b2 = p2.revenue - p2.cost;
                if(b1 == b2){
                    return Integer.compare(p1.id, p2.id);
                }else{
                    return Integer.compare(b2, b1);
                }
            }
        });

        for(int t = 0; t < Q-1; t ++){
            st = new StringTokenizer(input.readLine());
            req = Integer.parseInt(st.nextToken());
            int id;
            switch(req){
                case 200 :
                    id = Integer.parseInt(st.nextToken());
                    int revenue = Integer.parseInt(st.nextToken());
                    int dest = Integer.parseInt(st.nextToken());
                    make(id, revenue, dest);
                    break;

                case 300 :
                    id = Integer.parseInt(st.nextToken());
                    cancel(id);
                    break;

                case 400 :
                    output.append(sell()).append("\n");
                    break;

                case 500 :
                    start = Integer.parseInt(st.nextToken());
                    change(start, n);
                    break;

            }
        }
        System.out.print(output.toString());

    }
}