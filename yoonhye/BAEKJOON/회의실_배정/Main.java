package BAEKJOON.회의실_배정;

import java.io.*;
import java.util.*;

public class Main {
    static class Time{
        long start;
        long end;
        Time(long start, long end){
            this.start = start;
            this.end = end;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(input.readLine());
        List<Time> times = new ArrayList<>();
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(input.readLine());
            long start = Long.parseLong(st.nextToken());
            long end = Long.parseLong(st.nextToken());
            times.add(new Time(start, end));
        }

        Collections.sort(times, new Comparator<Time>() {
            @Override
            public int compare(Time o1, Time o2) {
                if(o1.start < o2.start){
                    return -1;
                }else if(o1.start == o2.start){
                    if(o1.end <= o2.end){
                        return -1;
                    }else{
                        return 1;
                    }
                }else{
                    return 1;
                }
            }
        });
        long prevStart = 0, prevEnd = 0;
        int cnt = 0;

        for(Time t : times){
            if(prevEnd > t.start && prevEnd > t.end){
                prevEnd = t.end;
            }else if(prevEnd <= t.start){
                prevEnd = t.end;
                prevStart = t.start;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
