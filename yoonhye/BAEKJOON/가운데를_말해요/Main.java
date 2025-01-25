package BAEKJOON.가운데를_말해요;

import java.util.*;
import java.io.*;

public class Main {
    static List<Integer> nums = new ArrayList<>();
    static void binarySearch(int target){
        int start = 0;
        int end = nums.size();
        int mid;
        if(end == 0){
            nums.add(target);
            return;
        }
        end -= 1;
        while(start<=end){
            mid = (start + end)/2;
            if(nums.get(mid) == target){
                nums.add(mid, target);
                return;
            }else if(nums.get(mid) > target){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
        nums.add(start, target);
    }
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();
        int N = Integer.parseInt(input.readLine());

        for(int i = 0; i<N; i++){
            binarySearch(Integer.parseInt(input.readLine()));
            int m = nums.size()/2;
            if(nums.size() % 2 == 0){
                output.append(nums.get(m-1)).append("\n");
            }else{
                output.append(nums.get(m)).append("\n");
            }
        }
        System.out.println(output.toString());
    }
}
