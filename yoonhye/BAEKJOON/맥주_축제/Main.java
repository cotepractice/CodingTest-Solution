package BAEKJOON.맥주_축제;

import java.io.*;
import java.util.*;

public class Main {
    static class Beer{
        int v;
        long c;
        Beer(int v, long c){
            this.v = v;
            this.c = c;
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Beer> info = new ArrayList<>();
        for(int i = 0; i<K; i++){
            st = new StringTokenizer(input.readLine());
            int v = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());
            info.add(new Beer(v, c));
        }

        //도수 레벨이 낮고, 선호도가 높은 순서대로 정렬
        Collections.sort(info, new Comparator<Beer>() {
            @Override
            public int compare(Beer o1, Beer o2) {
                if(o1.c < o2.c){
                    return -1;
                }else if(o1.c == o2.c && o1.v > o2.v){
                    return -1;
                }else{
                    return 1;
                }
            }
        });

        int prefer = 0;
        //낮은 선호도, 높은 도수 레벨이 우선 순위 높음
        PriorityQueue<Beer> queue = new PriorityQueue<>(new Comparator<Beer>() {
            @Override
            public int compare(Beer o1, Beer o2) {
                if(o1.v < o2.v){
                    return -1;
                }else if(o1.v == o2.v && o1.c > o2.c){
                    return -1;
                }else{
                    return 1;
                }
            }
        });
        for(int t = 0; t<K; t++){
            Beer beer = info.get(t);

            if(queue.size() < N){
                queue.add(beer);
                prefer += beer.v;
            }else{
                if(prefer >= M){
                    break;
                }else{
                    Beer b = queue.poll();
                    if(b.v < beer.v){
                        prefer = prefer - b.v + beer.v;
                        queue.add(beer);
                        if(prefer >= M){
                            break;
                        }
                    }else{
                        queue.add(b);
                    }
                }
            }
        }
        if(prefer >= M){
            long maxLevel = 0l;
            while(!queue.isEmpty()){
                maxLevel = Long.max(maxLevel, queue.poll().c);
            }
            System.out.println(maxLevel);
        }else{
            System.out.println(-1);
        }
    }
}
