package BAEKJOON.숫자의_합;
import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String str = sc.nextLine();
        String[] arr = str.split("");

        int sum = 0;
        for(int i=0; i<N; i++){
            sum += Integer.parseInt(arr[i]);
        }
        System.out.println(sum);

    }
}
