package SWEA.규영이와_인영이의_카드게임;

import java.util.*;
import java.io.*;

class Solution{
    public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static StringTokenizer st;
    public static StringBuilder output = new StringBuilder();
    public static List<Integer> gCards;
    public static Set<Integer> iCards;
    public static List<int[]> cases;
    public static int gWin;
    public static int gLose;
    public static void permutation(Integer arr[], int[] temp, int r, boolean[] visited) {
        if(r == 9) {
            fight(temp);
        }
        for(int i = 0; i<9; i++) {
            if(!visited[i]) {
                visited[i] = true;
                temp[r] = arr[i];
                permutation(arr, temp, r+1, visited);
                visited[i] = false;
            }
        }
    }
    public static void fight(int[] arr) {
        int gScore = 0;
        int iScore = 0;
        for(int i = 0; i<9; i++) {
            int gValue = gCards.get(i);
            int iValue = arr[i];
            if( gValue > iValue) {	//규영 승
                gScore += (gValue+iValue);
            }else if(gValue < iValue) {	//인영 승
                iScore += (gValue+iValue);
            }
        }
        if(gScore < iScore) {
            gLose++;
        }else if(gScore > iScore) {
            gWin++;
        }

    }
    public static void main(String args[]) throws Exception{

        int T = Integer.parseInt(input.readLine());

        for(int test_case = 1; test_case <= T; test_case++){
            st = new StringTokenizer(input.readLine());
            gCards = new ArrayList();	//규영이 카드
            iCards = new HashSet<>();	//인영이 카드
            for(int i = 1; i<=18; i++) {
                iCards.add(i);
            }
            for(int i = 0; i<9; i++) {
                gCards.add(Integer.parseInt(st.nextToken()));
            }
            iCards.removeAll(gCards);
            Integer[] iCardArr = iCards.toArray(new Integer[9]);
            cases = new ArrayList<>();
            gWin = 0;
            gLose = 0;

            permutation(iCardArr, new int[9], 0, new boolean[9]);

            output.append("#").append(test_case).append(" ")
                    .append(gWin).append(" ")
                    .append(gLose).append("\n");
        }
        System.out.println(output.toString());
    }
}