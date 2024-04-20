package BAEKJOON.구간_합_구하기;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        long[] num = new long[N+1];
        for(int i = 1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            num[i] = Long.parseLong(st.nextToken());
        }

        //1~999, 1000~1999, ... key값 : 1000으로 나눴을 때의 몫
        HashMap<Integer, Long> dp = new HashMap<>();
        int n = N/1000;
        for (int i = 0; i<=n; i++){
            int key = i;
            dp.put(key, (long)0);
            int start = key*1000;
            int end = key*1000+999;
            if (N<end){
                end = N;
            }
            for (int j=start; j<=end; j++){
                long value = dp.get(key);
                value += num[j];
                dp.put(key, value);
            }
        }

        ArrayList<Long> res = new ArrayList<>();
        for (int i=1; i<=(M+K); i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            //수를 바꿈
            if (a == 1){
                long original_value = num[b];
                int k = b/1000;
                long v = dp.get(k);
                v = v-original_value + c;
                dp.put(k, v);
                num[b] = c;

            } else { //합 구하기
                int k1 = b / 1000;
                int k2 = (int) c / 1000;
                if (k1 != k2) {
                    long sum1 = dp.get(k1);
                    long sum2 = 0;
                    long sum3 = dp.get(k2);
                    for (int j = k1 * 1000; j < b; j++) {
                        sum1 -= num[j];
                    }
                    for (int j = (k1+1); j<k2; j++){
                        sum2 += dp.get(j);
                    }

                    int end = k2 * 1000 + 999;
                    if (end > N){
                        end = N;
                    }
                    for (int j = (int) c + 1; j <= end; j++) {
                        sum3 -= num[j];
                    }
                    res.add(sum1 + sum2 + sum3);
                } else {
                    long sum = 0;
                    for (int j = b; j <= c; j++) {
                        sum += num[j];
                    }
                    res.add(sum);
                }
            }
        }
        for (int i = 0; i<K; i++){
            System.out.println(res.get(i));
        }
    }
}
