package BAEKJOON.니가_싫어_싫어_너무_싫어_싫어_오지_마_내게_찝쩍대지마_1;

import java.io.*;
import java.util.*;
public class Main {
    static class Time{
        long t;
        int value;
        Time(long t, int value){
            this.t = t;
            this.value = value;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        List<Time> times = new ArrayList<>();
        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(input.readLine());
            long Tem = Long.parseLong(st.nextToken());
            long Txm = Long.parseLong(st.nextToken());
            times.add(new Time(Tem, 1));
            times.add(new Time(Txm, -1));
        }

        Collections.sort(times, new Comparator<Time>() {
            @Override
            public int compare(Time o1, Time o2) {
                if(o1.t < o2.t){
                    return -1;
                } else if(o1.t == o2.t && o1.value < o2.value){
                    return -1;
                }else{
                    return 1;
                }
            }
        });

        int cnt = 0;
        int res = 0;
        long start = 0, end = 0;
        boolean status = false;
        for(int i = 0; i<times.size(); i++){
            Time t = times.get(i);
            cnt += t.value;
            if(end == t.t && t.value == 1){
                status = false;
            }
            if(res < cnt){
                start = t.t;
                res = cnt;
                status = false;
            } else if (t.value == -1 && res == cnt+1 && !status){
                status = true;
                end = t.t;
            }
        }
        System.out.println(res);
        System.out.println(start + " " + end);
    }
}
